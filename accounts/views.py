from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages as msgs
from django.db import IntegrityError
from django.views import View

from users.models import User

from accounts.serializers import CreateAccountSerializer
from accounts.services import AccountServices
from accounts.models import Account

from core.exceptions import SerializerException
from core.logger import Logger

import traceback

class AccountsView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            accounts = Account.objects.filter(db=request.user.db)
            context = { 'accounts': accounts }
            messages = list(msgs.get_messages(request))
            for message in messages:
                field = message.tags.split()[0]
                context[field] = message.message
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
    def get(self, request):
        try:
            users = User.objects.filter(db=request.user.db)
            context = { 'users': users }
            messages = list(msgs.get_messages(request))
            for message in messages:
                field = message.tags.split()[0]
                context[field] = message.message
            return render(request, 'accounts/create.html', context)
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
    
    def post(self, request):
        try:
            serializer = CreateAccountSerializer(data=request.POST)
            data = serializer.validated_data
            services = AccountServices(data)
            msgs.success(request, services.create_account(request), extra_tags='success')
            return redirect('accounts:home')
        except SerializerException as e:
            for field, error in e.errors.items():
                msgs.error(request, error, extra_tags=field)
            return redirect('accounts:create')
        except IntegrityError:
            msgs.error(
                request,
                'This user already has an account with this name',
                extra_tags='non_field_error'
            )
            return redirect('accounts:create')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class DeleteAccountView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            account = Account.objects.get(pk=pk)
            account.delete()
            msgs.success(request, 'Account deleted successfully', extra_tags='success')
            return redirect('accounts:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')