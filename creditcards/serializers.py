from django.http import QueryDict

from core.exceptions import SerializerException
from datetime import datetime
from decimal import Decimal

class CreateCreditCardSerializer:
    def __init__(self, data: QueryDict) -> None:
        self.name = data.get('name', None)
        self.account = data.get('account', None)
        self.due_day = data.get('due_day', None)
        self.limit = data.get('limit', None)
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_name()
        self.validate_account()
        self.validate_due_day()
        self.validate_limit()
        self.validated_data = {
            'name': self.name,
            'account': self.account,
            'due_day': self.due_day,
            'limit': self.limit
        }

    def validate_name(self) -> None:
        if not self.name:
            raise SerializerException({'name_error': 'The field is required'})
        
    def validate_account(self) -> None:
        if not self.account:
            raise SerializerException({'account_error': 'The field is required'})
        
    def validate_due_day(self) -> None:
        if not self.due_day:
            raise SerializerException({'due_day_error': 'The field is required'})
        try:
            self.due_day = int(self.due_day)
        except:
            raise SerializerException({'due_day_error': 'The field must be an integer'})
        if self.due_day < 1 or self.due_day > 31:
            raise SerializerException({'due_day_error': 'The field must be a number between 1 and 31'})
        
    def validate_limit(self) -> None:
        if not self.limit:
            raise SerializerException({'limit_error': 'The field is required'})
        try:
            self.limit = Decimal(self.limit)
        except:
            raise SerializerException({'limit_error': 'The field must be a number'})
        
class CreateCreditCardTransactionSerializer:
    def __init__(self, data: QueryDict) -> None:
        self.credit_card = data.get('credit_card', None)
        self.description = data.get('description', None)
        self.amount = data.get('amount', None)
        self.category = data.get('category', None)
        self.subcategory = data.get('subcategory', None)
        self.installments = data.get('installments', None)
        self.date = data.get('date', None)
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_credit_card()
        self.validate_description()
        self.validate_amount()
        self.validate_category()
        self.validate_subcategory()
        self.validate_installments()
        self.validate_date()
        self.validated_data = {
            'credit_card': self.credit_card,
            'description': self.description,
            'amount': self.amount,
            'category': self.category,
            'subcategory': self.subcategory,
            'installments': self.installments,
            'date': self.date
        }

    def validate_credit_card(self) -> None:
        if not self.credit_card:
            raise SerializerException({'credit_card_error': 'The field is required'})
        
    def validate_description(self) -> None:
        if not self.description:
            raise SerializerException({'description_error': 'The field is required'})
        
    def validate_amount(self) -> None:
        if not self.amount:
            raise SerializerException({'amount_error': 'The field is required'})
        try:
            self.amount = Decimal(self.amount)
        except:
            raise SerializerException({'amount_error': 'The field must be a number'})
        
    def validate_category(self) -> None:
        if not self.category:
            raise SerializerException({'category_error': 'The field is required'})
        
    def validate_subcategory(self) -> None:
        if not self.subcategory:
            raise SerializerException({'subcategory_error': 'The field is required'})
        
    def validate_installments(self) -> None:
        if not self.installments:
            raise SerializerException({'installments_error': 'The field is required'})
        try:
            self.installments = int(self.installments)
        except:
            raise SerializerException({'installments_error': 'The field must be an integer'})
        
    def validate_date(self) -> None:
        if not self.date:
            raise SerializerException({'date_error': 'The field is required'})
        
        try:
            self.date = datetime.strptime(self.date, '%Y-%m-%d').date()
        except:
            raise SerializerException({'date_error': 'The field must be a date in the format yyyy-mm-dd'})
        
class PayCreditCardSerializer:
    def __init__(self, data: QueryDict) -> None:
        print(data)
        self.credit_card = data.get('creditcard', None)
        self.amount = data.get('amount', None)
        self.account = data.get('account', None)
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_credit_card()
        self.validate_amount()
        self.validate_account()
        self.validated_data = {
            'credit_card': self.credit_card,
            'amount': self.amount,
            'account': self.account
        }

    def validate_credit_card(self) -> None:
        if not self.credit_card:
            raise SerializerException({'credit_card_error': 'The field is required'})
        
    def validate_amount(self) -> None:
        if not self.amount:
            raise SerializerException({'amount_error': 'The field is required'})
        try:
            self.amount = Decimal(self.amount)
        except:
            raise SerializerException({'amount_error': 'The field must be a number'})
        
    def validate_account(self) -> None:
        if not self.account:
            raise SerializerException({'account_error': 'The field is required'})