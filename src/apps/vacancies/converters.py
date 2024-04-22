from src.common.converters.base import BaseConverter
from src.common.converters.exceptions import IncorrectConverterArgument

from .models import Vacancy as VacancyModel
from .entities import VacancyEntity


class ORMVacancyConverter(BaseConverter):

    def handle(
        self,
        obj: VacancyModel | VacancyEntity,
    ) -> VacancyModel | VacancyEntity:
        '''
        Handle given object and convert it to needed type
        Entity -> DTO
        DTO -> Entity
        '''
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
        candidates = vacancy.interested_candidates.all()
        entity = VacancyEntity(
            id=vacancy.id,
            employer=vacancy.employer.to_entity(),
            interested_candidates=[cand.to_entity() for cand in candidates],
            title=vacancy.title,
            description=vacancy.description,
            company_name=vacancy.company_name,
            is_remote=vacancy.is_remote,
            required_experience=vacancy.required_experience,
            location=vacancy.location,
            required_skills=vacancy.required_skills,
            updated_at=vacancy.updated_at,
            created_at=vacancy.created_at,
        )
        return entity

    def convert_to_model(self, entity: VacancyEntity) -> VacancyModel:
        '''Convert entity into Django model'''
        model = VacancyModel(
            id=entity.id,
            employer=entity.employer,
            interested_candidates=entity.interested_candidates,
            title=entity.title,
            company_name=entity.company_name,
            description=entity.description,
            is_remote=entity.is_remote,
            required_experience=entity.required_experience,
            location=entity.location,
            required_skills=entity.required_skills,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
        return model
