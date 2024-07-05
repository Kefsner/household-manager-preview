from django.shortcuts import render, redirect
from django.contrib import messages as msgs
from django.views import View

from users.serializers import CreateUserSerializer
from users.services import UserServices
from users.models import User

from core.exceptions import SerializerException
from core.logger import Logger

import traceback

class UserView(View):
    def get(self, request):
        try:
            context = self._get(request)
            return render(request, 'users/home.html', context)
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
    @staticmethod
    def _get(request):
        users = User.objects.filter(db=request.user.db)
        return { 'users': users }

class CreateUserView(View):
    def post(self, request):
        try:
            serializer = CreateUserSerializer(data=request.POST)
            data = serializer.validated_data
            services = UserServices(data)
            msgs.success(request, services.create_user(request), extra_tags='success')
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
        
class DeleteUserView(View):
    def post(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            if user.is_staff:
                msgs.error(request, 'You cannot delete a staff user.')
                return redirect('users:home')
            user.delete()
            msgs.success(request, 'User deleted successfully.')
            return redirect('users:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')