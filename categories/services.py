from django.http import HttpRequest
from django.db.utils import IntegrityError
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
        subcategory.category = category
        subcategory.description = self.data['description']
        subcategory.save(request)
        return 'Subcategory created successfully.'

class DefaultCategoriesServices:
    def populate_categories(self, request):
        categories = [
            {
                'name': 'Housing',
                'type': 'expense'
            },
            {
                'name': 'Supermarket/Groceries',
                'type': 'expense'
            },
            {
                'name': 'Transportation',
                'type': 'expense'
            },
            {
                'name': 'Bills & Utilities',
                'type': 'expense'
            },
            {
                'name': 'Personal Care',
                'type': 'expense'
            },
            {
                'name': 'Entertainment',
                'type': 'expense'
            },
            {
                'name': 'Investments & Savings',
                'type': 'expense'
            },
            {
                'name': 'Salary',
                'type': 'income'
            }           
        ]
        for category in categories:
            try:
                Category.objects.create(
                    **category,
                    created_by=request.user,
                    db=request.user.db
                )
            except IntegrityError:
                pass

    def populate_subcategories(self, request):
        subcategories = [
            {
                'name': 'Rent',
                'category': Category.objects.get(name='Housing'),
                'description': 'Monthly rent payments'
            },
            {
                'name': 'Maintenance',
                'category': Category.objects.get(name='Housing'),
                'description': 'Repairs and improvements'
            },
            {
                'name': 'Utilities',
                'category': Category.objects.get(name='Housing'),
                'description': 'Electricity, water, gas, internet, etc'
            },
            {
                'name': 'Food',
                'category': Category.objects.get(name='Supermarket/Groceries'),
                'description': 'Everyday food and groceries'
            },
            {
                'name': 'Household',
                'category': Category.objects.get(name='Supermarket/Groceries'),
                'description': 'Cleaning supplies, toiletries, etc'
            },
            {
                'name': 'Beverages',
                'category': Category.objects.get(name='Supermarket/Groceries'),
                'description': 'Alcoholic and non-alcoholic drinks'
            },
            {
                'name': 'Car',
                'category': Category.objects.get(name='Transportation'),
                'description': 'Gas, maintenance, insurance, etc'
            },
            {
                'name': 'Public/Shared Transportation',
                'category': Category.objects.get(name='Transportation'),
                'description': 'Bus, train, uber, etc'
            },
            {
                'name': 'Electricity',
                'category': Category.objects.get(name='Bills & Utilities'),
                'description': 'Monthly electricity bill'
            },
            {
                'name': 'Water',
                'category': Category.objects.get(name='Bills & Utilities'),
                'description': 'Monthly water bill'
            },
            {
                'name': 'Internet',
                'category': Category.objects.get(name='Bills & Utilities'),
                'description': 'Monthly internet bill'
            },
            {
                'name': 'Phone',
                'category': Category.objects.get(name='Bills & Utilities'),
                'description': 'Monthly phone bill'
            },
            {
                'name': 'Health',
                'category': Category.objects.get(name='Personal Care'),
                'description': 'Medicine, doctor appointments, etc'
            },
            {
                'name': 'Beauty',
                'category': Category.objects.get(name='Personal Care'),
                'description': 'Haircuts, cosmetics, etc'
            },
            {
                'name': 'Clothing',
                'category': Category.objects.get(name='Personal Care'),
                'description': 'Clothes, shoes, etc'
            },
            {
                'name': 'Dining Out',
                'category': Category.objects.get(name='Entertainment'),
                'description': 'Restaurants, fast food, cafes, etc'
            },
            {
                'name': 'Movies',
                'category': Category.objects.get(name='Entertainment'),
                'description': 'Cinema, streaming services, etc'
            },
            {
                'name': 'Hobbies',
                'category': Category.objects.get(name='Entertainment'),
                'description': 'Books, games, music, etc'
            },
            {
                'name': 'Savings',
                'category': Category.objects.get(name='Investments & Savings'),
                'description': 'Money set aside in savings account',
            },
            {
                'name': 'Investments',
                'category': Category.objects.get(name='Investments & Savings'),
                'description': 'Stocks, bonds, etc'
            },
            {
                'name': 'Salary',
                'category': Category.objects.get(name='Salary'),
                'description': 'Monthly salary'
            }
        ]    
        for subcategory in subcategories:
            try:
                Subcategory.objects.create(
                    **subcategory,
                    created_by=request.user,
                    db=request.user.db
                )
            except IntegrityError:
                pass

    def run(self, request):
        self.populate_categories(request)
        self.populate_subcategories(request)        