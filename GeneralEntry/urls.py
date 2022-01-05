from django.urls import path
from .views import GeneralEntryCreateView, GeneralEntryListView

urlpatterns = [
    path('', GeneralEntryListView.as_view()),
    path('add/', GeneralEntryCreateView.as_view()),
]