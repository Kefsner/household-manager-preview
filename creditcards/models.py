from django.db import models
from django.db.models import Sum

from core.models import MetaData

from accounts.models import Account
from categories.models import Category, Subcategory

from dateutil.relativedelta import relativedelta

from decimal import Decimal

import datetime
import holidays

class CreditCard(MetaData):
    name = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    due_day = models.IntegerField()
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_limit = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ['name', 'account']

    @staticmethod
    def adjust_for_holidays_and_weekends(date: datetime.date) -> datetime.date:
        while date in holidays.Brazil() or date.weekday() in [5, 6]:
            date += datetime.timedelta(days=1)
        return date

    @property
    def next_due_date(self):
        today = datetime.date.today()
        due = datetime.date(today.year, today.month, self.due_day)
        if today > due:
            due += relativedelta(months=1)
        return self.adjust_for_holidays_and_weekends(due)
    
    #TODO: Rework these methods so the next_bill_amount is calculated with a month offset,
    #      hence we can display any month's bill amount
    
    @property
    def next_bill_amount(self):
        next_due_date = self.next_due_date
        if next_due_date:
            next_bill_amount = CreditCardInstallment.objects.filter(
                credit_card_transaction__credit_card=self,
                due_date=next_due_date,
                paid=False
            ).aggregate(total_amount=Sum('amount'))['total_amount'] or Decimal('0.00')
            return next_bill_amount.quantize(Decimal('0.01'))
        return Decimal('0.00')

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