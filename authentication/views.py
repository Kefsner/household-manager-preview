from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages as msgs
from django.contrib.auth import logout
from django.views import View

from authentication.exceptions import InvalidCredentials
from authentication.serializers import LoginSerializer
from authentication.services import LoginServices

from core.exceptions import SerializerException
from core.logger import Logger

import traceback

class LoginView(View):
    template_name = 'authentication/authentication.html'
    def get(self, request):
        try:
            if request.user.is_authenticated:
                return redirect('base:home')
            messages = list(msgs.get_messages(request))
            context = {}
            if messages and messages[-1].message == 'register':
                context['is_register'] = True
                messages.pop()
            for message in messages:
                field = message.tags.split()[0]
                context[field] = message.message
            return render(request, self.template_name, context)
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
    
    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            serializer = LoginSerializer(data=request.POST)
            data = serializer.validated_data
            services = LoginServices(data)
            services.login(request)
            return redirect('base:home')
        except (SerializerException, InvalidCredentials) as e:
            for field, error in e.errors.items():
                msgs.error(request, error, extra_tags=field)
            return redirect('authentication:login')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class LogoutView(View):
    def get(self, request):
        try:
            logout(request)
            return redirect('authentication:login')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')