from django.http import QueryDict

from core.exceptions import SerializerException

class CreateUserSerializer:
    """
    This class is responsible for validating the data that comes from the request
    for the registration of a new user.

    It creates a dictionary with the validated data and fills the errors dictionary, if any,
    after calling the validate_data method.
    """
    def __init__(self, data: QueryDict, db: str) -> None:
        self.db = db
        self.username = data.get('username', None)
        self.password = data.get('password', None)
        self.password_confirm = data.get('password_confirm', None)
        self.is_staff = data.get('is_staff', False) == 'True'
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_username()
        self.validate_password()
        self.validate_password_confirm()
        self.validated_data = {
            'username': self.username,
            'password': self.password,
            'is_staff': self.is_staff
        }

    def validate_username(self) -> None:
        if not self.username:
            raise SerializerException({'username': 'The field is required'})
        
    def validate_password(self) -> None:
        if not self.password:
            raise SerializerException({'password': 'The field is required'})
        
    def validate_password_confirm(self) -> None:
        if not self.password_confirm:
            raise SerializerException({'password_confirm': 'The field is required'})
        
        if self.password != self.password_confirm:
            raise SerializerException({
                'password': 'The passwords do not match',
                'password_confirm': 'The passwords do not match'
            })