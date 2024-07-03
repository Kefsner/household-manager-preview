from django.urls import path
from django.conf import settings

from users.views import *

app_name = 'users'

urlpatterns = [
    path('', UserView.as_view(), name='home'),
    path('create/', CreateUserView.as_view(), name='create'),
    path(f'{settings.DELETE_URL}/<int:pk>/', DeleteUserView.as_view(), name='delete'),
]