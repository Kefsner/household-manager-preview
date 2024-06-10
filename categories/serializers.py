from django.http import QueryDict

from core.exceptions import SerializerException
from categories.models import Category

class CreateCategorySerializer:
    def __init__(self, data: QueryDict) -> None:
        self.name = data.get('name', None)
        self.type = data.get('type', None)
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_name()
        self.validate_type()
        self.validated_data = {
            'name': self.name,
            'type': self.type
        }

    def validate_name(self) -> None:
        if not self.name:
            raise SerializerException({'name_error': 'The field is required'})
        
    def validate_type(self) -> None:
        if not self.type:
            raise SerializerException({'type_error': 'The field is required'})
        if self.type not in ['income', 'expense']:
            raise SerializerException({'type_error': 'The field must be either income or expense'})
        
class AddSubcategorySerializer:
    def __init__(self, data: QueryDict) -> None:
        self.name = data.get('name', None)
        self.description = data.get('description', None)
        self.validate_data()

    def validate_data(self) -> None:
        self.validate_name()
        self.validate_description()
        self.validated_data = {
            'name': self.name,
            'description': self.description
        }

    def validate_name(self) -> None:
        if not self.name:
            raise SerializerException({'name_error': 'The field is required'})

    def validate_description(self) -> None:
        if not self.description:
            raise SerializerException({'description_error': 'The field is required'})
        if len(self.description) > 255:
            raise SerializerException({'description_error': 'The field must be less than 255 characters'})
        