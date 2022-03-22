from django.urls import path
from .views import PartyCreateView, PartyListView, PartyDetailView

urlpatterns = [
    path('add/', PartyCreateView.as_view(success_url='')),
    path('', PartyListView.as_view(), name='party_list'),
    path('<pk>/', PartyDetailView.as_view()),
]