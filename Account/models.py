from django.db import models
from itertools import chain

# Create your models here.
class Account(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


    def entries(self):
        entries = list(chain(self.generalentry_set.all(), self.productentry_set.all()))
        entries.sort(key=lambda x: x.date)

        balance = 0
        for entry in entries:
            entry.balance = balance = entry.credit - entry.debit + balance


        return entries