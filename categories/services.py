from django.http import HttpRequest

from categories.models import Category, Subcategory

class CategoryServices:
    def __init__(self, data):
        self.data = data

    def create_category(self, request: HttpRequest) -> str:
        category = Category()
        category.name = self.data['name']
        category.type = self.data['type']
        category.save(request)
        return 'Category created successfully.'
    
    def add_subcategory(self, request: HttpRequest, category: Category) -> str:
        subcategory = Subcategory()
        subcategory.name = self.data['name']
        print(category)
        subcategory.category = category
        subcategory.description = self.data['description']
        subcategory.save(request)
        return 'Subcategory created successfully.'