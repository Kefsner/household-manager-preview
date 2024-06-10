from django.urls import path

from creditcards.views import *

app_name = 'creditcards'

urlpatterns = [
    path('', CreditCardView.as_view(), name='home'),
    path('create/', CreateCreditCardView.as_view(), name='create'),
]