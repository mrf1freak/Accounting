from django.db import models
from Product.models import Packing, Product
from Account.models import Account
from Accounting.models import Entry

class ProductEntry(Entry):

    @property
    def credit(self):
        CREDIT = ["Purchase"]
        if self.type in CREDIT:
            return self.total()
        return 0

    @property
    def debit(self):
        DEBIT = ["Sale"]
        if self.type in DEBIT:
            return self.total()
        return 0

    def total(self):
        query_set = self.entryitem_set.all().annotate(sum=models.Sum(models.F('packing__size') * models.F('quantity') * models.F('price')))
        
        if len(query_set) == 0:
            return 0
        
        items_sum = sum([x.sum for x in query_set])
        return items_sum


class EntryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    packing = models.ForeignKey(Packing, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()
    entry = models.ForeignKey(ProductEntry, on_delete=models.CASCADE)

    @property
    def total_quantity(self):
        return self.packing.size * self.quantity

    @property
    def total_price(self):
        return self.total_quantity * self.price
