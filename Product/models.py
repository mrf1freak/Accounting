from django.db import models
from django.urls import reverse

class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Packing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def final_quantity(self):
        total_quantity = self.quantity
        items = self.entryitem_set.all()
        for item in items:
            print(item.quantity)
            if item.entry.credit > 0:
                total_quantity -= item.quantity
            else:
                total_quantity += item.quantity

        return total_quantity

        
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.product.pk})

    
