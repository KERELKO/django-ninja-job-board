from src.common.converters.exceptions import IncorrectConverterArgument
from src.apps.profiles.entities.employers import EmployerEntity

from src.apps.profiles.models.employers import EmployerProfile

from src.common.converters.base import BaseConverter


class ORMEmployerConverter(BaseConverter):
    def handle(
        self,
        obj: EmployerProfile | EmployerEntity,
    ) -> EmployerProfile | EmployerEntity:
        if obj.__class__ == EmployerEntity:
            return self.convert_to_model(obj)
        elif obj.__class__ == EmployerProfile:
            return self.convert_to_entity(obj)
        else:
            raise IncorrectConverterArgument(
                obj,
                choices=[EmployerProfile, EmployerEntity],
            )

    def convert_to_entity(
        self,
        model: EmployerProfile,
    ) -> EmployerEntity:
        return EmployerEntity(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
            company_name=model.company_name,
        )

    def convert_to_model(
        self,
        entity: EmployerEntity,
    ) -> EmployerProfile:
        return EmployerProfile(
            id=entity.id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            email=entity.email,
            company_name=entity.company_name,
        )
