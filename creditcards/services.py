from django.http import HttpRequest

from django.db import transaction
from creditcards.models import CreditCard, CreditCardTransaction, CreditCardInstallment
from creditcards.exceptions import CreditCardException
from accounts.models import Account
from categories.models import Category, Subcategory

from dateutil.relativedelta import relativedelta
from decimal import Decimal, getcontext
import datetime

getcontext().prec = 2

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
    def generate_due_dates(due_day: int, date: datetime.date, total_installments: int):
        due = datetime.date(date.year, date.month, due_day)
        due = CreditCard.adjust_for_holidays_and_weekends(due)
        if date > due:
            due += relativedelta(months=1)
        closing_date = due - relativedelta(days=7)
        if date > closing_date:
            due += relativedelta(months=1)
        due = CreditCard.adjust_for_holidays_and_weekends(due)
        yield due  # Yield the first installment's due date
        for _ in range(1, total_installments):
            due += relativedelta(months=1)
            due = CreditCard.adjust_for_holidays_and_weekends(due)
            yield due  # Yield the next installment's due date

    def create_transaction(self, request: HttpRequest) -> str:
        with transaction.atomic():
            _transaction = CreditCardTransaction()
            credit_card = CreditCard.objects.get(id=self.data['credit_card'])
            if credit_card.remaining_limit < self.data['amount']:
                raise CreditCardException('Insufficient limit.')
            credit_card.remaining_limit -= self.data['amount']
            credit_card.save(request)
            _transaction.credit_card = credit_card
            _transaction.description = self.data['description']
            _transaction.amount = self.data['amount']
            _transaction.category = Category.objects.get(id=self.data['category'])
            _transaction.subcategory = Subcategory.objects.get(id=self.data['subcategory']) if self.data['subcategory'] else None
            _transaction.date = self.data['date']
            _transaction.installments = self.data['installments']
            _transaction.save(request)
            
            basic_installment_amount = (_transaction.amount / _transaction.installments).quantize(Decimal('0.01'))
            total_calculated_amount = basic_installment_amount * _transaction.installments
            remainder = _transaction.amount - total_calculated_amount
            for i, due_date in enumerate(CreditCardServices.generate_due_dates(
                                            credit_card.due_day,
                                            self.data['date'],
                                            _transaction.installments), start=1):
                if due_date < datetime.date.today():
                    raise CreditCardException('Due date cannot be in the past.')
                installment = CreditCardInstallment()
                installment.credit_card_transaction = _transaction
                installment.amount = basic_installment_amount
                if i == _transaction.installments:
                    installment.amount += remainder
                installment.due_date = due_date
                installment.installment_number = i
                installment.save(request)
        return 'Transaction created successfully.'
    
    def pay_credit_card(self, request: HttpRequest, credit_card: CreditCard) -> str:
        with transaction.atomic():
            # Pay only if is closed. That is, today is between the closing date and the due date.
            if not (
                (credit_card.next_due_date - relativedelta(days=7) <= datetime.date.today()) and
                (datetime.date.today() <= credit_card.next_due_date)
            ):
                raise CreditCardException('Credit card is not closed.')
            next_bill_amount = credit_card.next_bill_amount
            account = Account.objects.get(id=self.data['account'])
            if account.balance < self.data['amount']:
                raise CreditCardException('Insufficient balance.')
            account.balance -= self.data['amount']
            account.save(request)
            credit_card.remaining_limit += self.data['amount']
            if next_bill_amount == self.data['amount']:
                self._pay_credit_card(request, credit_card)
            else:
                self._pay_credit_card(request, credit_card, partial=True)
            credit_card.save(request)
        return 'Credit card paid successfully.'
    
    def _pay_credit_card(self, request: HttpRequest, credit_card: CreditCard, partial: bool = False) -> None:
        for installment in CreditCardInstallment.objects.filter(
            credit_card_transaction__credit_card=credit_card,
            paid=False,
            due_date=credit_card.next_due_date):
            installment.paid = True
            installment.save(request)
        if partial:
            remaining_amount = credit_card.next_bill_amount - self.data['amount']
            installment = CreditCardInstallment()
            installment.amount = remaining_amount
            installment.paid = False
            installment.credit_card_transaction = CreditCardTransaction()
            installment.credit_card_transaction.credit_card = credit_card
            installment.credit_card_transaction.description = 'Partial payment'
            installment.credit_card_transaction.amount = remaining_amount
            installment.credit_card_transaction.category = self._get_partial_payment_category(request)
            installment.credit_card_transaction.date = datetime.date.today()
            installment.credit_card_transaction.installments = 1
            installment.credit_card_transaction.save(request)
            installment.due_date = credit_card.next_due_date
            installment.installment_number = 1
            installment.save(request)
            if remaining_amount > 0:
                print('Add interest/fee here.')

    @staticmethod
    def _get_partial_payment_category(request: HttpRequest) -> Category:
        try:
            category = Category.objects.get(name='partial_payment')
        except Category.DoesNotExist:
            category = Category()
            category.name = 'partial_payment'
            category.type = 'system'
            category.save(request)
        finally:
            return category