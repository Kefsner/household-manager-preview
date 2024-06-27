from django.db import models

from core.models import MetaData

class Category(MetaData):
    CATEGORY_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
        ('transfer', 'Transfer')
    )
    name = models.CharField(max_length=100, unique=True, null=True)
    type = models.CharField(choices=CATEGORY_TYPES, max_length=10)

class Subcategory(MetaData):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        unique_together = ('name', 'category')