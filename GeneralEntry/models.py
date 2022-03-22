from django.db import models
from Accounting.models import Entry

class GeneralEntry(Entry):
    ENTRY_CHOICES = [
        ("Debit", "Debit"),
        ("Credit", "Credit")
    ]

    type = models.CharField(max_length=40, choices=ENTRY_CHOICES)
    amount = models.IntegerField()

    
    @property
    def credit(self):
        CREDIT = ["Credit"]
        if self.type in CREDIT:
            return self.amount
        return 0

    @property
    def debit(self):
        DEBIT = ["Debit"]
        if self.type in DEBIT:
            return self.amount
        return 0


