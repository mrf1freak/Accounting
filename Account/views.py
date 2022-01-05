from django.shortcuts import render
from django import http
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Account
from GeneralEntry.models import GeneralEntry
import datetime

class AccountCreateView(CreateView):
    model = Account
    fields = '__all__'

    def form_valid(self, form):
        amount = int(self.request.POST.get("amount", 0))

        type = "Credit"
        if amount < 0:
            type = "Debit"
            amount = -amount

        account = form.save(commit=False)
    
        entry = GeneralEntry(description="Initial Balance", amount=amount, user=self.request.user, type=type, account=account, date=datetime.datetime.today().strftime("%Y-%m-%d"))

        form.save()
        entry.save()

        return http.HttpResponseRedirect('/account')


class AccountListView(ListView):
    model = Account
    fields = '__all__'

class AccountDetailView(DetailView):
    model = Account
