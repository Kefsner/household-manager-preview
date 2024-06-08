class CoreException(Exception):
    def __init__(self, errors: dict) -> None:
        self.errors = errors

class SerializerException(CoreException):
    pass