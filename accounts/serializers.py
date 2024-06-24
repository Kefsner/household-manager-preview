from django.http import QueryDict

from core.exceptions import SerializerException

from decimal import Decimal

class CreateAccountSerializer:
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
        
class CreateTransactionSerializer:
    def __init__(self, data: QueryDict) -> None:
        self.type = data.get('type', None)
        self.account = data.get('account', None)
        self.amount = data.get('amount', None)
        self.category = data.get('category', None)
        self.subcategory = data.get('subcategory', None)
        self.description = data.get('description', None)
        self.date = data.get('date', None)
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_type()
        self.validate_account()
        self.validate_amount()
        self.validate_category()
        self.validate_subcategory()
        self.validate_description()
        self.validate_date()
        self.validated_data = {
            'type': self.type,
            'account': self.account,
            'amount': self.amount,
            'category': self.category,
            'subcategory': self.subcategory,
            'description': self.description,
            'date': self.date
        }

    def validate_type(self) -> None:
        if not self.type:
            raise SerializerException({'type_error': 'The field is required'})
        if self.type not in ['expense', 'income']:
            raise SerializerException({'type_error': 'The field must be either "expense" or "income"'})

    def validate_account(self) -> None:
        if not self.account:
            raise SerializerException({'account_error': 'The field is required'})
        
    def validate_amount(self) -> None:
        if not self.amount:
            raise SerializerException({'amount_error': 'The field is required'})
        if len(str(self.amount).split('.')[0]) > 10:
            raise SerializerException({'amount_error': 'The field must have at most 10 digits'})
        try:
            self.amount = Decimal(self.amount)
            self.amount = abs(self.amount)
        except:
            raise SerializerException({'amount_error': 'The field must be a number'})
        
    def validate_category(self) -> None:
        if not self.category:
            raise SerializerException({'category_error': 'The field is required'})
        
    def validate_subcategory(self) -> None:
        if not self.subcategory:
            raise SerializerException({'subcategory_error': 'The field is required'})
        
    def validate_description(self) -> None:
        if not self.description:
            raise SerializerException({'description_error': 'The field is required'})
        
    def validate_date(self) -> None:
        if not self.date:
            raise SerializerException({'date_error': 'The field is required'})
