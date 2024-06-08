from django.urls import path
from django.conf import settings

from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('', AccountsView.as_view(), name='home'),
    path('create/', CreateAccountView.as_view(), name='create'),
    path(f'{settings.DELETE_URL}/<int:pk>/', DeleteAccountView.as_view(), name='delete'),

    path('transactions/create/', CreateTransactionView.as_view(), name='create_transaction'),
]