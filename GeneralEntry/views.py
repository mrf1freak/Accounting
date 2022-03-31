from email.policy import default
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django import forms
from django.urls import reverse
from datetime import date
from django.http import HttpResponseRedirect
from Account.models import Account
from .models import GeneralEntry


class GeneralEntryCreateView(CreateView):
    class EntryForm(forms.ModelForm):
        class Meta:
            model = GeneralEntry
            exclude = ('user',)
            widgets = {
                'date': forms.DateInput(attrs={'type': 'date', 'value': date.today()})
            }

    form_class = EntryForm
    template_name = "generalentry_form.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('generalentry_list')


class GeneralEntryListView(ListView):
    model = GeneralEntry