from users.models import User
from core.models import DB

class UserServices:
    def __init__(self, data: dict) -> None:
        self.data = data

    def create_user(self) -> dict:
        user = User()
        user.username = self.data['username']
        user.set_password(self.data['password'])
        db = DB.objects.create()
        user.db = db
        user.save()
        return 'User created successfully. You can now login.'