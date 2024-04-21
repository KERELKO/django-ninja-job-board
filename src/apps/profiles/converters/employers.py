from src.common.converters.exceptions import IncorrectConverterArgument
from src.apps.profiles.entities.profiles import (
    EmployerProfile as EmployerProfileEntity,
)
from src.apps.profiles.models.profiles import (
    EmployerProfile as EmployerProfileModel,
)
from src.common.converters.base import BaseConverter


class ORMEmployerProfileConverter(BaseConverter):
    def handle(
        self,
        obj: EmployerProfileModel | EmployerProfileEntity,
    ) -> EmployerProfileModel | EmployerProfileEntity:
        if obj.__class__ == EmployerProfileEntity:
            return self.convert_to_model(obj)
        elif obj.__class__ == EmployerProfileModel:
            return self.convert_to_entity(obj)
        else:
            raise IncorrectConverterArgument(
                obj,
                choices=[EmployerProfileModel, EmployerProfileEntity],
            )

    def convert_to_entity(
        self,
        model: EmployerProfileModel,
    ) -> EmployerProfileEntity:
        return EmployerProfileEntity(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
            company_name=model.company_name,
        )

    def convert_to_model(
        self,
        entity: EmployerProfileEntity,
    ) -> EmployerProfileModel:
        return EmployerProfileModel(
            id=entity.id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            email=entity.email,
            company_name=entity.company_name,
        )
