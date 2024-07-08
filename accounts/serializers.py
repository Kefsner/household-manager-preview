from decimal import Decimal
from django.http import QueryDict
from core.exceptions import SerializerException

from categories.models import Category, Subcategory
from accounts.models import Account
from users.models import User

from datetime import datetime
from decimal import Decimal

class CreateAccountSerializer:
    def __init__(self, data: QueryDict, db: str) -> None:
        self.db = db
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
            raise SerializerException({'user': 'This field is required'})
        if not User.objects.filter(id=self.user, db=self.db).exists():
            raise SerializerException({'user': 'Invalid user'})
        
    def validate_name(self) -> None:
        if not self.name:
            raise SerializerException({'name': 'This field is required'})
        if Account.objects.filter(name=self.name, user=self.user, db=self.db).exists():
            raise SerializerException({'name': 'This user already has an account with this name'})
        if len(self.name) > 100:
            raise SerializerException({'name': 'This field must have at most 100 characters'})
        
    def validate_initial_balance(self) -> None:
        if not self.initial_balance:
            raise SerializerException({'initial_balance': 'This field is required'})
        try:
            self.initial_balance = Decimal(self.initial_balance)
        except:
            raise SerializerException({'initial_balance': 'The field must be a number'})

class BaseTransactionSerializer:
    def __init__(self, data: QueryDict, db: str) -> None:
        self.db = db
        self.account = data.get('account', None)
        self.amount = data.get('amount', None)
        self.description = data.get('description', None)
        self.date = data.get('date', None)
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_amount()
        self.validate_account()
        self.validate_description()
        self.validate_date()
        self.validated_data = {
            'account': self.account,
            'amount': self.amount,
            'description': self.description,
            'date': self.date
        }

    def validate_account(self) -> None:
        if not self.account:
            raise SerializerException({'account': 'This field is required'})
        if not Account.objects.filter(id=self.account, db=self.db).exists():
            raise SerializerException({'account': 'Invalid account'})

    def validate_amount(self) -> None:
        if not self.amount:
            raise SerializerException({'amount': 'This field is required'})
        if len(str(self.amount).split('.')[0]) > 10:
            raise SerializerException({'amount': 'This field must have at most 10 digits'})
        try:
            self.amount = Decimal(self.amount)
            self.amount = abs(self.amount)
        except:
            raise SerializerException({'amount': 'This field must be a number'})

    def validate_description(self) -> None:
        if not self.description:
            raise SerializerException({'description': 'This field is required'})

    def validate_date(self) -> None:
        if not self.date:
            raise SerializerException({'date': 'This field is required'})
        try:
            self.date = datetime.strptime(self.date, '%d-%m-%Y').date()
        except:
            raise SerializerException({'date': 'Invalid date format. Must be DD-MM-YYYY'})

class CreateTransactionSerializer(BaseTransactionSerializer):
    def __init__(self, data: QueryDict, db: str) -> None:
        super().__init__(data, db)
        self.type = data.get('type', None)
        self.category = data.get('category', None)
        self.subcategory = data.get('subcategory', None)
        self.validate_transaction_data()
        self.validated_data['type'] = self.type
        self.validated_data['category'] = self.category
        self.validated_data['subcategory'] = self.subcategory

    def validate_transaction_data(self) -> None:
        self.validate_type()
        self.validate_category()
        if self.subcategory:
            self.validate_subcategory()

    def validate_type(self) -> None:
        if not self.type:
            raise SerializerException({'type': 'This field is required'})
        if self.type not in ['expense', 'income']:
            raise SerializerException({'type': 'Invalid type. Must be either "expense" or "income"'})

    def validate_category(self) -> None:
        if not self.category:
            raise SerializerException({'category': 'This field is required'})
        if not Category.objects.filter(id=self.category, db=self.db).exists():
            raise SerializerException({'category': 'Invalid category'})
        category = Category.objects.get(id=self.category)
        if category.type != self.type:
            raise SerializerException({'category': 'Invalid category type'})
        
    def validate_subcategory(self) -> None:
        if not Subcategory.objects.filter(id=self.subcategory, db=self.db).exists():
            raise SerializerException({'subcategory': 'Invalid subcategory'})
        subcategory = Subcategory.objects.get(id=self.subcategory)
        if subcategory.category != self.category:
            raise SerializerException({'subcategory': 'Invalid subcategory'})


class CreateTransferSerializer(BaseTransactionSerializer):
    def __init__(self, data: QueryDict) -> None:
        super().__init__(data)
        self.to_account = data.get('to_account', None)
        self.validate_to_account()
        self.validated_data['to_account'] = self.to_account

    def validate_to_account(self) -> None:
        if not self.to_account:
            raise SerializerException({'to_account': 'This field is required'})
        if self.to_account == self.account:
            raise SerializerException({'to_account': 'Transfer to the same account is not allowed'})
        if not Account.objects.filter(id=self.to_account, db=self.db).exists():
            raise SerializerException({'to_account': 'Invalid account'})
