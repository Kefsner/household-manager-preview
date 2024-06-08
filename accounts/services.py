from django.http import HttpRequest

from users.models import User

from accounts.models import Account

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