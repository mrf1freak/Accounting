from django.forms import formset_factory
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render, HttpResponse

from Account.models import Account

from .forms import EntryItemForm, EntryForm
from .models import ProductEntry
import json



class EntryItemCreateView(View):
    def __init__(self):
        super()
        self.context = {
            'entryItemForm': EntryItemForm,
            'entryForm': EntryForm
        }

    def get(self, request):
        return render(request, 'entry_form.html', self.context)

    def post(self, request):
        form = EntryForm(request.POST)
        if not form.is_valid():
            self.context['entryForm'] = form
            return render(request, 'entry_form.html', self.context)

        form.cleaned_data['user'] = request.user
        form.cleaned_data['account'] = Account.objects.get_or_create(code='000', defaults={'name': 'SALE'})
        form_instance = form.save()


        items_json = json.loads(request.POST['items'])
        
        items = []
        for item in items_json:
            item['entry'] = form_instance.id
            entryItemForm = EntryItemForm(item)
            if not entryItemForm.is_valid():

                return render(request, 'entry_form.html', self.context)

            items.append(entryItemForm)
                

        for item in items:
            item.save()

        return render(request, 'entry_form.html', self.context)
        

class EntryListView(ListView):
    model = ProductEntry

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        object_list = context['object_list']
        balance = 0
        for object in object_list:
            object.balance = balance = balance + object.credit - object.debit

        return context


class EntryDetailView(DetailView):
    model = ProductEntry