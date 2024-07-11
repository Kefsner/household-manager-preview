from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages as msgs
from django.views import View

from users.serializers import CreateUserSerializer
from users.services import UserServices
from users.models import User

from core.exceptions import SerializerException
from core.logger import Logger

import traceback

class UserView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            users = User.objects.filter(db=request.user.db)
            context = { 'users': users }
            return render(request, 'users/home.html', context)
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')

class CreateUserView(View):
    def post(self, request):
        try:
            serializer = CreateUserSerializer(data=request.POST)
            data = serializer.validated_data
            services = UserServices(data)
            msgs.success(request, services.create_user(request), extra_tags='success')
            if request.user.is_authenticated:
                return redirect('users:home')
            return redirect('authentication:login')
        except SerializerException as e:
            for field, error in e.errors.items():
                extra_tags = 'page ' + field
                msgs.error(request, error, extra_tags=extra_tags)
            msgs.info(request, 'register')
            return redirect('users:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class DeleteUserView(LoginRequiredMixin, View):
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