from django.http import QueryDict

from core.exceptions import SerializerException

from decimal import Decimal

class CreateAccountSerializer:
    """
    This class is responsible for validating the data that comes from the request
    for the creation of a new account.

    It creates a dictionary with the validated data and fills the errors dictionary, if any,
    after calling the validate_data method.
    """
    def __init__(self, data: QueryDict) -> None:
        self.user = data.get('user', None)
        self.name = data.get('name', None)
        self.initial_balance = data.get('initial_balance', None)
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_user()
        self.validate_name()
        self.validate_initial_balance()
        self.validated_data = {
            'user': self.user,
            'name': self.name,
            'initial_balance': self.initial_balance
        }

    def validate_user(self) -> None:
        if not self.user:
            raise SerializerException({'user_error': 'The field is required'})
        
    def validate_name(self) -> None:
        if not self.name:
            raise SerializerException({'name_error': 'The field is required'})
        
    def validate_initial_balance(self) -> None:
        if not self.initial_balance:
            raise SerializerException({'initial_balance_error': 'The field is required'})
        try:
            self.initial_balance = Decimal(self.initial_balance)
        except:
            raise SerializerException({'initial_balance_error': 'The field must be a number'})