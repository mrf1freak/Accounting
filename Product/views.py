from django.http.response import JsonResponse
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Packing, Product
from django.shortcuts import get_object_or_404
from django.core import serializers

class ProductListView(ListView):
    model = Product
    

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    

    def get_success_url(self):
        return '/product'

class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    

    def get_success_url(self):
        return '/product'


class PackingCreateView(CreateView):
    model = Packing
    fields = ['size', 'quantity']
    success_url=''

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        form.instance.product = product
        return super(PackingCreateView, self).form_valid(form)


class PackingDetailView(DetailView):
    model = Packing

    def get_context_data(self, **kwargs):
        context = super(PackingDetailView, self).get_context_data(**kwargs)
        

        context['entryitem_set'] = None

class PackingListJSONView(View):

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        packings = list(Packing.objects.filter(product=product).values())

        return JsonResponse(packings, safe=False)
