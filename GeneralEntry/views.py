from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django import forms
from datetime import date
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
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()        
        return http.HttpResponseRedirect(self.get_success_url())


class GeneralEntryListView(ListView):
    model = GeneralEntry