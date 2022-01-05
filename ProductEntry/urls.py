from django.urls import path
from .views import EntryItemCreateView, EntryListView, EntryDetailView

urlpatterns = [
    path('', EntryListView.as_view()),
    path('add/', EntryItemCreateView.as_view()),
    path('<int:pk>', EntryDetailView.as_view()),
]