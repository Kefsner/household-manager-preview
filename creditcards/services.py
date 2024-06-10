from django.http import HttpRequest

from creditcards.models import CreditCard
from accounts.models import Account

class CreditCardServices:
    def __init__(self, data):
        self.data = data

    def create_credit_card(self, request: HttpRequest) -> str:
        credit_card = CreditCard()
        credit_card.name = self.data['name']
        credit_card.account = Account.objects.get(id=self.data['account'])
        credit_card.due_day = self.data['due_day']
        credit_card.limit = self.data['limit']
        credit_card.remaining_limit = self.data['limit']
        credit_card.save(request)
