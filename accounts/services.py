from django.http import HttpRequest

from users.models import User
from accounts.models import Account, Transaction
from categories.models import Category, Subcategory

class AccountServices:
    def __init__(self, data):
        self.data = data
        
    def create_account(self, request: HttpRequest) -> str:
        account = Account()
        account.name = self.data['name']
        account.user = User.objects.get(id=self.data['user'])
        account.initial_balance = self.data['initial_balance']
        account.balance = self.data['initial_balance']
        account.save(request)
        return 'Account created successfully.'
    
    def create_transaction(self, request: HttpRequest) -> str:
        transaction = Transaction()
        transaction.account = Account.objects.get(id=self.data['account'])
        transaction.value = self.data['value']
        transaction.category = Category.objects.get(id=self.data['category'])
        transaction.subcategory = Subcategory.objects.get(id=self.data['subcategory']) if self.data['subcategory'] else None
        transaction.description = self.data['description']
        transaction.date = self.data['date']
        transaction.save(request)
        return 'Transaction created successfully.'