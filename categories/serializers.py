from django.http import QueryDict

from core.exceptions import SerializerException

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