import imp
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse

from .models import Party

class PartyCreateView(CreateView):
    model = Party
    fields = '__all__'

    def get_success_url(self):
        return reverse('party_list')


class PartyListView(ListView):
    model = Party
    fields = '__all__'

class PartyDetailView(DetailView):
    model = Party
