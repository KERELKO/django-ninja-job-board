from src.common.converters.base import BaseConverter
from src.common.converters.exceptions import IncorrectConverterArgument

from ..models.vacancies import Vacancy as VacancyModel
from ..entities.vacancies import Vacancy as VacancyEntity


# TODO: reduce hard coding
class ORMVacancyConverter(BaseConverter):

    def handle(
        self,
        obj: VacancyModel | VacancyEntity
    ) -> VacancyModel | VacancyEntity:
        if obj.__class__ == VacancyModel:
            return self.convert_to_entity(obj)
        elif obj.__class__ == VacancyEntity:
            return self.convert_to_model(obj)
        else:
            raise IncorrectConverterArgument(
                choices=[VacancyModel.__name__, VacancyEntity.__name__]
            )

    def convert_to_entity(self, vacancy: VacancyModel) -> VacancyEntity:
        '''Convert Django model into entity'''
        entity = VacancyEntity(
            id=vacancy.id,
            title=vacancy.title,
            description=vacancy.description,
            remote=vacancy.remote,
            required_experience=vacancy.required_experience,
            location=vacancy.location,
            required_skills=vacancy.required_skills,
            company_name=vacancy.company_name,
            updated_at=vacancy.updated_at,
            created_at=vacancy.created_at,
        )
        return entity

    def convert_to_model(self, entity: VacancyEntity) -> VacancyModel:
        '''Convert entity into Django model'''
        model = VacancyModel(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            remote=entity.remote,
            company_name=entity.company_name,
            required_experience=entity.required_experience,
            location=entity.location,
            required_skills=entity.required_skills,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
        return model
