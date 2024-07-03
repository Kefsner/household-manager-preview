from django.http import HttpRequest

from core.models import DB

from users.models import User

class UserServices:
    def __init__(self, data: dict) -> None:
        self.data = data

    def create_user(self, request: HttpRequest) -> str:
        user = User()
        user.username = self.data['username']
        user.set_password(self.data['password'])
        if self.data['is_staff']:
            user.is_staff = True
            db = DB.objects.create()
            user.db = db
        else:
            user.is_staff = False
            user.db = request.user.db
        user.save()
        return 'User registered successfully. You can now login.'