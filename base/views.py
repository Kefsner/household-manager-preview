from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now
from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from decimal import Decimal

from accounts.models import Account, Transaction

class BaseView(LoginRequiredMixin, View):
    def get(self, request):
        accounts = Account.objects.filter(db=request.user.db)
        balance_sum = accounts.aggregate(Sum('balance'))['balance__sum'] or Decimal('0')

        today = now().date()
        first_day_of_month = today.replace(day=1)

        # Filter transactions for the current month
        monthly_transactions = Transaction.objects.filter(
            account__db=request.user.db,
            date__gte=first_day_of_month,
            date__lte=today
        )

        total_expenses = monthly_transactions.filter(amount__lt=0).aggregate(Sum('amount'))['amount__sum'] or Decimal('0')
        total_income = monthly_transactions.filter(amount__gt=0).aggregate(Sum('amount'))['amount__sum'] or Decimal('0')
        
        context = {
            'balance_sum': balance_sum,
            'total_expenses': abs(total_expenses),
            'total_income': total_income,
            'balance': total_income + total_expenses,
        }
        return render(request, 'base/home.html', context)