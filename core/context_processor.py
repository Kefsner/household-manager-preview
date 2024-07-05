from django.contrib import messages as msgs

from categories.models import Category, Subcategory
from creditcards.models import CreditCard
from accounts.models import Account

from datetime import datetime

def context(request):
    if request.user.is_authenticated:
        categories = Category.objects.filter(db=request.user.db)
        subcategories = Subcategory.objects.filter(db=request.user.db)
        accounts = Account.objects.filter(db=request.user.db)
        creditcards = CreditCard.objects.filter(db=request.user.db)
        today = datetime.now().date().strftime('%Y-%m-%d')
        form_errors = request.session.get('form_errors')
        context = {
            'categories': categories,
            'subcategories': subcategories,
            'accounts': accounts,
            'creditcards': creditcards,
            'today': today,
            'form_errors': form_errors
        }
        messages = list(msgs.get_messages(request))
        if messages and messages[-1].message == 'register':
            context['is_register'] = True
            messages.pop()
        for message in messages:
            field = message.tags.split()[0]
            context[field] = message.message
        return context
    return {}
