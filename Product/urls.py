from django.urls import path
from .views import PackingDetailView, ProductDetailView, ProductListView, ProductCreateView, PackingCreateView, PackingListJSONView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('add/', ProductCreateView.as_view()),
    path('<pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('<pk>/packing/add', PackingCreateView.as_view(), name='packing-create'),
    path('packing/<pk>', PackingDetailView.as_view(), name='packing-detail'),
    path('<pk>/packing', PackingListJSONView.as_view(), name='packing-json')

]