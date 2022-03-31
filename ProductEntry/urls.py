from django.urls import path
from .views import EntryItemCreateView, EntryItemCreateView2, EntryListView, EntryDetailView

urlpatterns = [
    path('', EntryListView.as_view(), name='productentry_list'),
    path('add/', EntryItemCreateView2.as_view()),
    path('<int:pk>', EntryDetailView.as_view()),
]