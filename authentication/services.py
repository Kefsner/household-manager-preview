from django.http import HttpRequest
from django.contrib.auth import login
from django.http import QueryDict

from users.models import User

from authentication.exceptions import InvalidCredentials

class LoginServices:
    def __init__(self, data: QueryDict) -> None:
        self.username = data.get('username', None)
        self.password = data.get('password', None)

    def login(self, request: HttpRequest) -> None:
        try:
            user = User.objects.get(username=self.username)
            if user and user.check_password(self.password):
                login(request, user)
                return
            raise InvalidCredentials({'non_field_error': 'Invalid credentials'})
        except User.DoesNotExist:
            raise InvalidCredentials({'non_field_error': 'Invalid credentials'})