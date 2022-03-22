from django import forms
from .models import EntryItem, ProductEntry
from datetime import date



class EntryForm(forms.ModelForm):
    class Meta:
        model = ProductEntry
        fields = '__all__'

        exclude = ['user', 'account']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': date.today()})
        }


class EntryItemForm(forms.ModelForm):
    class Meta:
        model = EntryItem
        fields = '__all__'
        widgets = {
            'product': forms.Select(attrs={'id':'products', 'v-model': 'product', 'v-on:change': 'changeItem'}),
            'entry': forms.HiddenInput()
        }