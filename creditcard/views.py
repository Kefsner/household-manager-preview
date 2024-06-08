from django.contrib import messages as msgs
from django.shortcuts import render
from django.views import View

from creditcard.models import CreditCard

from core.logger import Logger

import traceback

class CreditCardView(View):
    def get(self, request):
        try:
            credit_cards = CreditCard.objects.filter(db=request.user.db)
            context = { 'credit_cards': credit_cards }
            messages = list(msgs.get_messages(request))
            for message in messages:
                field = message.tags.split()[0]
                context[field] = message.message
            return render(request, 'creditcard/home.html', context)
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')