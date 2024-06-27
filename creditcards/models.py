from django.db import models
from django.db.models import Sum, Min

from core.models import MetaData

from accounts.models import Account
from categories.models import Category, Subcategory

class CreditCard(MetaData):
    name = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    due_day = models.IntegerField()
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_limit = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ['name', 'account']

    @property
    def next_due_day(self):
        next_due_date = CreditCardInstallment.objects.filter(
            credit_card_transaction__credit_card=self,
            paid=False
        ).aggregate(next_due_date=Min('due_date'))['next_due_date']
        return next_due_date
    
    @property
    def next_bill_amount(self):
        next_due_date = self.next_due_day
        if next_due_date:
            next_bill_amount = CreditCardInstallment.objects.filter(
                credit_card_transaction__credit_card=self,
                due_date=next_due_date,
                paid=False
            ).aggregate(total_amount=Sum('amount'))['total_amount'] or 0
            return next_bill_amount
        return 0

class CreditCardTransaction(MetaData):
    description = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='transactions')
    installments = models.IntegerField()

class CreditCardInstallment(MetaData):
    credit_card_transaction = models.ForeignKey(CreditCardTransaction, on_delete=models.CASCADE, related_name='transaction_installments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    installment_number = models.IntegerField()
    paid = models.BooleanField(default=False)