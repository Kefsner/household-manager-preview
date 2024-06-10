from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.utils import timezone

from accounts.models import Account
from categories.models import Category, Subcategory

class BaseView(LoginRequiredMixin, View):
    def get(self, request):
        balance_sum = Account.objects.filter(
            db=request.user.db
            ).aggregate(Sum('balance'))['balance__sum']
        today = timezone.now().date().strftime('%Y-%m-%d')
        categories = Category.objects.filter(db=request.user.db)
        subcategories = Subcategory.objects.filter(db=request.user.db)
        context = {
            'balance_sum': balance_sum,
            'today': today,
            'categories': categories,
            'subcategories': subcategories,
            }
        return render(request, 'base/home.html', context)