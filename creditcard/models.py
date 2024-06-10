from django.db import models
from core.models import MetaData

from accounts.models import Account
from categories.models import Category, Subcategory

class CreditCard(MetaData):
    name = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    due_day = models.IntegerField()
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_limit = models.DecimalField(max_digits=10, decimal_places=2)

class CreditCardTransaction(MetaData):
    description = models.CharField(max_length=100, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='transactions')
    installments = models.IntegerField()

class CreditCardInstallment(MetaData):
    credit_card_transaction = models.ForeignKey(CreditCardTransaction, on_delete=models.CASCADE, related_name='transaction_installments')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    installment_number = models.IntegerField()
    paid = models.BooleanField(default=False)