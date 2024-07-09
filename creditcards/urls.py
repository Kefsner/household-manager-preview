from django.urls import path
from django.conf import settings

from creditcards.views import *

app_name = 'creditcards'

urlpatterns = [
    path('', CreditCardView.as_view(), name='home'),
    path('create/', CreateCreditCardView.as_view(), name='create'),
    path(f'{settings.DELETE_URL}/creditcard/<int:pk>/', DeleteCreditCardView.as_view(), name='delete'),

    path('transactions/create/', CreateTransactionView.as_view(), name='create_transaction'),

    path('<int:pk>/pay/', PayCreditCardView.as_view(), name='pay'),
]