from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages as msgs
from django.db import IntegrityError
from django.views import View

from categories.serializers import CreateCategorySerializer
from categories.services import CategoryServices
from categories.models import Category, Subcategory

from core.logger import Logger
from core.exceptions import SerializerException

import traceback

class CategoriesView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            categories = Category.objects.filter(db=request.user.db)
            context = { 'categories': categories }
            messages = list(msgs.get_messages(request))
            for message in messages:
                field = message.tags.split()[0]
                context[field] = message.message
            return render(request, 'categories/home.html', context)
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')

class CreateCategoryView(LoginRequiredMixin, View):    
    def post(self, request):
        try:
            serializer = CreateCategorySerializer(data=request.POST)
            data = serializer.validated_data
            services = CategoryServices(data)
            msgs.success(request, services.create_category(request))
            return redirect('categories:home')
        except SerializerException as e:
            for field, error in e.errors.items():
                msgs.error(request, error, extra_tags=field)
            return redirect('categories:home')
        except IntegrityError:
            msgs.error(request, 'Category already exists.')
            return redirect('categories:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                data=request.POST,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')
        
class DeleteCategoryView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            msgs.success(request, 'Category deleted successfully.')
            return redirect('categories:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                data=request.POST,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')