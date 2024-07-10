from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.shortcuts import render
from django.db.models import Sum
from django.views import View

from accounts.models import Transaction, Account
from creditcards.models import CreditCard, CreditCardTransaction

import json

class BaseView(LoginRequiredMixin, View):
    def get(self, request):
        today = now().date()
        current_month = today.month
        current_year = today.year

        # Aggregate expenses by category for the current month and year
        expenses_by_category = Transaction.objects.filter(
            account__user=request.user,
            date__month=current_month,
            date__year=current_year,
            amount__lt=0
        ).values('category__name').annotate(total=Sum('amount')).order_by('category__name')

        expense_data = {
            'labels': [exp['category__name'] for exp in expenses_by_category],
            'data': [float(abs(exp['total'])) for exp in expenses_by_category],
        }
        total_expenses = sum(expense_data['data'])

        # Similarly, aggregate incomes by category
        incomes_by_category = Transaction.objects.filter(
            account__user=request.user,
            date__month=current_month,
            date__year=current_year,
            amount__gt=0
        ).values('category__name').annotate(total=Sum('amount')).order_by('category__name')

        income_data = {
            'labels': [inc['category__name'] for inc in incomes_by_category],
            'data': [float(inc['total']) for inc in incomes_by_category],
        }
        total_income = sum(income_data['data'])

        context = {
            'expense_data_json': mark_safe(json.dumps(expense_data)),
            'income_data_json': mark_safe(json.dumps(income_data)),
            'total_income': total_income,
            'total_expenses': total_expenses,
        }

        # Last 5 transactions
        transactions = Transaction.objects.filter(db=request.user.db).order_by('-date')[:5]
        context['transactions'] = transactions

        # Last 5 credit card transactions
        creditcard_transactions = CreditCardTransaction.objects.filter(db=request.user.db).order_by('-date')[:5]
        context['creditcard_transactions'] = creditcard_transactions

        # Total in accounts
        accounts = Account.objects.filter(db=request.user.db)
        total = sum([account.balance for account in accounts])
        context['total_in_accounts'] = total

        # Total next credit card bill
        creditcards = CreditCard.objects.filter(db=request.user.db)
        total = sum([creditcard.next_bill_amount for creditcard in creditcards])
        context['total_next_credit_card_bill'] = total
        return render(request, 'base/home.html', context)