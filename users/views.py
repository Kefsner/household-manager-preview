from django.shortcuts import render, redirect
from django.contrib import messages as msgs
from django.views import View

from users.serializers import RegisterSerializer
from users.services import UserServices

from core.exceptions import SerializerException
from core.logger import Logger

import traceback

class CreateUserView(View):
    template_name = 'authentication/authentication.html'
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.POST)
            data = serializer.validated_data
            services = UserServices(data)
            msgs.success(request, services.create_user(), extra_tags='success')
            return redirect('authentication:login')
        except SerializerException as e:
            for field, error in e.errors.items():
                msgs.error(request, error, extra_tags=field)
            msgs.info(request, 'register')
            return redirect('authentication:login')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
