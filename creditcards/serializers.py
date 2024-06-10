from django.http import QueryDict

from core.exceptions import SerializerException

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
        
    def validate_limit(self) -> None:
        if not self.limit:
            raise SerializerException({'limit_error': 'The field is required'})
        try:
            self.limit = Decimal(self.limit)
        except:
            raise SerializerException({'limit_error': 'The field must be a number'})