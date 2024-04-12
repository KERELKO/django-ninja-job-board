from src.core.common.converters.converters import BaseConverter
from src.core.common.converters.exceptions import IncorrectConverterArgument

from .models import Vacancy as VacancyModel
from .entities import Vacancy as VacancyEntity


class ORMVacancyConverter(BaseConverter):

    def handle(self, obj: VacancyModel | VacancyEntity):
        if obj.__class__ == VacancyModel:
            ...
        elif obj.__class__ == VacancyEntity:
            ...
        else:
            raise IncorrectConverterArgument(
                choices=[VacancyModel.__name__, VacancyEntity.__name__]
            )

    def convert_to_entity(self, vacancy: VacancyModel) -> VacancyEntity:
        '''Convert Django model into Entity'''
        # Hardcoding
        entity = VacancyEntity(
            id=vacancy.id,
            title=vacancy.title,
            description=vacancy.description,
            slug=vacancy.slug,
            remote=vacancy.remote,
            open=vacancy.open,
            required_experience=vacancy.required_experience,
            location=vacancy.location,
            required_skills=vacancy.required_skills,
            company_name=vacancy.company_name,
            updated_at=vacancy.updated_at,
            created_at=vacancy.created_at,
        )
        return entity

    def convert_to_model(self, entity: VacancyEntity) -> VacancyModel:
        model = VacancyModel(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            remote=entity.remote,
            company_name=entity.company_name,
            slug=entity.slug,
            required_experience=entity.required_experience,
            location=entity.location,
            open=entity.open,
            required_skills=entity.required_skills,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
        return model
