from django.urls import path
from django.conf import settings

from categories.views import *

app_name = 'categories'

urlpatterns = [
    path('', CategoriesView.as_view(), name='home'),
    path('create/', CreateCategoryView.as_view(), name='create'),
    path(f'{settings.DELETE_URL}/<int:pk>/', DeleteCategoryView.as_view(), name='delete'),
]