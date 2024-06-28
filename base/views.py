from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages as msgs
from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from accounts.models import Account

class BaseView(LoginRequiredMixin, View):
    def get(self, request):
        accounts = Account.objects.filter(db=request.user.db)
        balance_sum = accounts.aggregate(Sum('balance'))['balance__sum']
        context = {
            'balance_sum': balance_sum,
            }
        return render(request, 'base/home.html', context)