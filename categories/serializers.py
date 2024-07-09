from django.http import QueryDict

from core.exceptions import SerializerException

class CreateCategorySerializer:
    def __init__(self, data: QueryDict, db: str) -> None:
        self.db = db
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
            raise SerializerException({'name': 'The field is required'})
        
    def validate_type(self) -> None:
        if not self.type:
            raise SerializerException({'type': 'The field is required'})
        if self.type not in ['income', 'expense']:
            raise SerializerException({'type': 'The field must be either income or expense'})
        
class CreateSubcategorySerializer:
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
            raise SerializerException({'name': 'The field is required'})

    def validate_description(self) -> None:
        if len(self.description) > 255:
            raise SerializerException({'description': 'The field must be less than 255 characters'})
        