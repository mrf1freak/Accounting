from django.db import models
from Account.models import Account
from Party.models import Party
from django.contrib.auth.models import User

class Entry(models.Model):
    ENTRY_CHOICES = [
        ("Sale", "Sale"),
        ("Purchase", "Purchase")
    ]

    date = models.DateField()
    description = models.CharField(max_length=120)
    type = models.CharField(max_length=40, choices=ENTRY_CHOICES)
    party = models.ForeignKey(Party, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    
    class Meta:
        abstract = True
        ordering = ['date']
        
