from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages as msgs
from django.db import IntegrityError
from django.views import View

from users.models import User

from accounts.serializers import CreateAccountSerializer, CreateTransactionSerializer
from accounts.exceptions import InsufficientFundsException
from accounts.serializers import CreateTransferSerializer
from accounts.services import AccountServices
from accounts.models import Account

from core.exceptions import SerializerException
from core.utils import next_page
from core.logger import Logger

import traceback

class AccountsView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            users = User.objects.filter(db=request.user.db)
            context = { 'users': users }
            return render(request, 'accounts/home.html', context)
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')

class CreateAccountView(LoginRequiredMixin, View):    
    def post(self, request):
        try:
            serializer = CreateAccountSerializer(
                data=request.POST,
                db=request.user.db
            )
            data = serializer.validated_data
            services = AccountServices(data)
            msgs.success(request, services.create_account(request))
            return redirect('accounts:home')
        except SerializerException as e:
            for field, error in e.errors.items():
                extra_tags = 'page ' + field
                msgs.error(request, error, extra_tags=extra_tags)
            return redirect('accounts:home')
        except IntegrityError:
            msgs.error(
                request,
                'This user already has an account with this name',
            )
            return redirect('accounts:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                data=request.POST,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class DeleteAccountView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            account = Account.objects.get(pk=pk)
            account.delete()
            msgs.success(request, 'Account deleted successfully')
            return redirect('accounts:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                data=request.POST,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')

class CreateTransactionView(LoginRequiredMixin, View):    
    def post(self, request):
        try:
            serializer = CreateTransactionSerializer(
                data=request.POST,
                db=request.user.db
            )
            data = serializer.validated_data
            services = AccountServices(data)
            msgs.success(request, services.create_transaction(request))
            return redirect(next_page(request))
        except SerializerException as e:
            for field, error in e.errors.items():
                form_type = request.POST.get('type') # 'expense' or 'income'
                extra_tags = form_type + ' ' + field if form_type else field
                msgs.error(request, error, extra_tags=extra_tags)
            return redirect(next_page(request))
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                data=request.POST,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class CreateTransferView(LoginRequiredMixin, View):    
    def post(self, request):
        try:
            serializer = CreateTransferSerializer(
                data=request.POST,
                db=request.user.db
            )
            data = serializer.validated_data
            services = AccountServices(data)
            msgs.success(request, services.create_transfer(request))
            return redirect(next_page(request))
        except SerializerException as e:
            for field, error in e.errors.items():
                msgs.error(request, error, extra_tags=field)
            return redirect(next_page(request))
        except InsufficientFundsException as e:
            msgs.error(request, str(e))
            return redirect(next_page(request))
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                data=request.POST,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')