from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages as msgs
from django.db import IntegrityError
from django.views import View

from categories.serializers import CreateCategorySerializer, AddSubcategorySerializer
from categories.services import CategoryServices, DefaultCategoriesServices
from categories.models import Category, Subcategory

from core.logger import Logger
from core.exceptions import SerializerException

import traceback

class CategoriesView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            return render(request, 'categories/home.html')
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
        
class AddSubcategoryView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = AddSubcategorySerializer(data=request.POST)
            data = serializer.validated_data
            services = CategoryServices(data)
            msgs.success(request, services.add_subcategory(request, category))
            return redirect('categories:home')
        except SerializerException as e:
            for field, error in e.errors.items():
                msgs.error(request, error, extra_tags=field)
            return redirect('categories:home')
        except IntegrityError as e:
            msgs.error(request, 'Subcategory already exists in this category.')
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
        
class DeleteSubcategoryView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            subcategory = Subcategory.objects.get(pk=pk)
            subcategory.delete()
            msgs.success(request, 'Subcategory deleted successfully.')
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
        
class CreateDefaultCategoriesView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            services = DefaultCategoriesServices()
            services.run(request)
            msgs.success(request, 'Default categories created successfully.')
            return redirect('categories:home')
        except Exception as e:
            logger = Logger()
            logger.log(
                exception=e,
                request=request,
                traceback=traceback.format_exc()
            )
            return render(request, 'core/error.html')