from django.db import models

from users.models import User

from categories.models import Category, Subcategory

from core.models import MetaData

class Account(MetaData):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='owned_accounts')
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('name', 'user')

class Transaction(MetaData):
    description = models.CharField(max_length=100, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.DO_NOTHING, null=True)
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)

class Transfer(MetaData):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    from_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='transfers_sent')
    to_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='transfers_received')