from src.common.converters.base import BaseConverter


# TODO: to finish this converter,
# and replace usage of the 'to_entity' on 'handle' in Service Layer
class ORMEmployerProfileConverter(BaseConverter):
    def handle(self, obj):
        ...

    def convert_to_entity(self, obj):
        return super().convert_to_entity(obj)
