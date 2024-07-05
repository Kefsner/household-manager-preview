from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.shortcuts import render
from django.db.models import Sum
from django.views import View

from accounts.models import Transaction

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
        return render(request, 'base/home.html', context)