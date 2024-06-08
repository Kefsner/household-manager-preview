from django.http import QueryDict

from core.exceptions import SerializerException

class LoginSerializer:
    """
    This class is responsible for validating the data that comes from the request
    for the login of a user.
    """
    def __init__(self, data: QueryDict) -> None:
        self.username = data.get('username', None)
        self.password = data.get('password', None)
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_username()
        self.validate_password()
        self.validated_data = {
            'username': self.username,
            'password': self.password
        }

    def validate_username(self) -> None:
        if not self.username:
            raise SerializerException({'username_error': 'The field is required'})
        
    def validate_password(self) -> None:
        if not self.password:
            raise SerializerException({'password_error': 'The field is required'})