from django.http import HttpRequest

from django.db import transaction
from creditcards.models import CreditCard, CreditCardTransaction, CreditCardInstallment
from accounts.models import Account
from categories.models import Category, Subcategory

from dateutil.relativedelta import relativedelta
import datetime
import holidays

class CreditCardServices:
    def __init__(self, data):
        self.data = data

    def create_credit_card(self, request: HttpRequest) -> str:
        with transaction.atomic():
            credit_card = CreditCard()
            credit_card.name = self.data['name']
            credit_card.account = Account.objects.get(id=self.data['account'])
            credit_card.due_day = self.data['due_day']
            credit_card.limit = self.data['limit']
            credit_card.remaining_limit = self.data['limit']
            credit_card.save(request)
            return 'Credit card created successfully.'
    
    @staticmethod
    def adjust_for_holidays_and_weekends(date: datetime.date) -> datetime.date:
        while date in holidays.Brazil() or date.weekday() in [5, 6]:
            date += datetime.timedelta(days=1)
        return date
    
    @staticmethod
    def calculate_due_date(due_day: int, month: datetime.date) -> datetime.date:
        due_date = month.replace(day=due_day) + relativedelta(months=1)
        due_date = CreditCardServices.adjust_for_holidays_and_weekends(due_date)
        closing_date = due_date - relativedelta(days=7) # 7 for nubank, for instance
        today = datetime.date.today()
        if today > closing_date:
            due_date = due_date + relativedelta(months=1)
            due_date = CreditCardServices.adjust_for_holidays_and_weekends(due_date)
        return due_date

    def create_transaction(self, request: HttpRequest) -> str:
        with transaction.atomic():
            _transaction = CreditCardTransaction()
            credit_card = CreditCard.objects.get(id=self.data['credit_card'])
            credit_card.remaining_limit -= self.data['amount']
            credit_card.save(request)
            _transaction.credit_card = credit_card
            _transaction.description = self.data['description']
            _transaction.amount = self.data['amount']
            _transaction.category = Category.objects.get(id=self.data['category'])
            _transaction.subcategory = Subcategory.objects.get(id=self.data['subcategory']) if self.data['subcategory'] else None
            date = self.data['date']
            _transaction.date = date
            _transaction.installments = self.data['installments']
            _transaction.save(request)
            amount_per_installment = _transaction.amount / _transaction.installments
            for i in range(_transaction.installments):
                due_date = CreditCardServices.calculate_due_date(
                    credit_card.due_day,
                    date
                )
                installment = CreditCardInstallment()
                installment.credit_card_transaction = _transaction
                installment.amount = amount_per_installment
                installment.due_date = due_date
                installment.installment_number = i + 1
                installment.save(request)
                date += relativedelta(months=1)
            return 'Transaction created successfully.'