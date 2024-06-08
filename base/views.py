from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from accounts.models import Account

class BaseView(LoginRequiredMixin, View):
    def get(self, request):
        balance_sum = Account.objects.filter(
            user=request.user
            ).aggregate(Sum('balance'))['balance__sum']
        context = {
            'balance_sum': balance_sum
        }
        return render(request, 'base/home.html', context)