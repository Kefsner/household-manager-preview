from django.http import HttpRequest

from categories.models import Category

class CategoryServices:
    def __init__(self, data):
        self.data = data

    def create_category(self, request: HttpRequest) -> str:
        category = Category()
        category.name = self.data['name']
        category.type = self.data['type']
        category.save(request)
        return 'Category created successfully.'