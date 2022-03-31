from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import View
from django.views.generic import FormView
from django.shortcuts import render, HttpResponse
from django.http.response import HttpResponseBadRequest
from django.db import transaction
from django.urls import reverse


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


class EntryItemCreateView2(FormView):
    template_name = "entry_form.html"
    form_class = EntryForm
    

    def get_context_data(self, **kwargs):
        return {
            'entryItemForm': EntryItemForm,
            'entryForm': EntryForm
        }

    @transaction.atomic
    def form_valid(self, form):
        account, _created = Account.objects.get_or_create(code='000', defaults={'name': 'SALE'})
        form.instance.account = account
        form.instance.user = self.request.user
  
        obj = form.save()
        item_objects = self.get_item_objects()

        for item_object in item_objects:
            item_object['entry'] = obj.id
            item = EntryItemForm(item_object)
            item.save()

        return HttpResponseRedirect(reverse('productentry_list'))

    def get_item_objects(self):
        return json.loads(self.request.POST['items'])
        

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