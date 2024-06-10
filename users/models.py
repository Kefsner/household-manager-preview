from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import DB

class User(AbstractUser):
    db = models.ForeignKey(DB, on_delete=models.CASCADE)