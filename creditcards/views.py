from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages as msgs
from django.db import IntegrityError
from django.views import View

from creditcards.serializers import CreateCreditCardSerializer, PayCreditCardSerializer
from creditcards.serializers import CreateCreditCardTransactionSerializer
from creditcards.exceptions import CreditCardException
from creditcards.services import CreditCardServices
from creditcards.models import CreditCard

from core.exceptions import SerializerException
from core.logger import Logger

import traceback

class CreditCardView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            return render(request, 'creditcard/home.html')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class CreateCreditCardView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            serializer = CreateCreditCardSerializer(data=request.POST)
            data = serializer.validated_data
            services = CreditCardServices(data)
            msgs.success(request, services.create_credit_card(request))
            return redirect('creditcards:home')
        except SerializerException as e:
            for field, error in e.errors.items():
                msgs.error(request, error, extra_tags=field)
            return redirect('creditcards:home')
        except IntegrityError:
            msgs.error(request, 'Credit card already exists.')
            return redirect('creditcards:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                data=request.POST,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class DeleteCreditCardView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            credit_card = CreditCard.objects.get(id=pk)
            credit_card.delete()
            msgs.success(request, 'Credit card deleted successfully')
            return redirect('creditcards:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class CreateTransactionView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            serializer = CreateCreditCardTransactionSerializer(data=request.POST)
            data = serializer.validated_data                   
            services = CreditCardServices(data)
            msgs.success(request, services.create_transaction(request))
            return redirect('base:home')
        except CreditCardException as e:
            msgs.error(request, str(e))
            return redirect('base:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                data=request.POST,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class PayCreditCardView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            serializer = PayCreditCardSerializer(data=request.POST)
            data = serializer.validated_data
            services = CreditCardServices(data)
            services.pay_credit_card(request)
            msgs.success(request, 'Credit card paid successfully')
            return redirect('creditcards:home')
        except CreditCardException as e:
            msgs.error(request, str(e))
            return redirect('creditcards:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')