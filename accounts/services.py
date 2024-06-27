from django.http import HttpRequest
from django.db import transaction

from users.models import User

from accounts.exceptions import TransferException
from accounts.models import Account, Transaction

from categories.models import Category, Subcategory

class AccountServices:
    def __init__(self, data):
        self.data = data
        
    def create_account(self, request: HttpRequest) -> str:
        with transaction.atomic():
            account = Account()
            account.name = self.data['name']
            account.user = User.objects.get(id=self.data['user'])
            account.initial_balance = self.data['initial_balance']
            account.balance = self.data['initial_balance']
            account.save(request)
        return 'Account created successfully.'
    
    def create_transaction(self, request: HttpRequest) -> str:
        with transaction.atomic():
            _transaction = Transaction()
            _transaction.account = Account.objects.get(id=self.data['account'])
            _transaction.amount = self.data['amount']
            if self.data['type'] == 'expense':
                _transaction.amount *= -1
            _transaction.category = Category.objects.get(id=self.data['category'])
            _transaction.subcategory = Subcategory.objects.get(id=self.data['subcategory']) if self.data['subcategory'] else None
            _transaction.description = self.data['description']
            _transaction.date = self.data['date']
            _transaction.save(request)
            _transaction.account.balance += _transaction.amount
            _transaction.account.save(request)
        return 'Transaction created successfully.'
    
    def create_transfer(self, request: HttpRequest) -> str:
        with transaction.atomic():
            from_account = Account.objects.get(id=self.data['account'])
            to_account = Account.objects.get(id=self.data['to_account'])
            amount = self.data['amount']
            if from_account.balance < amount:
                raise TransferException({'amount_error': 'Insufficient funds'})
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save(request)
            to_account.save(request)
        return 'Transfer created successfully.'