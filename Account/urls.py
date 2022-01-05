from django.urls import path
from .views import AccountCreateView, AccountListView, AccountDetailView

urlpatterns = [
    path('add/', AccountCreateView.as_view(success_url='')),
    path('', AccountListView.as_view()),
    path('<pk>/', AccountDetailView.as_view()),
]