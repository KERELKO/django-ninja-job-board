from src.common.converters.base import BaseConverter
from src.common.converters.exceptions import IncorrectConverterArgument

from .models import Vacancy as VacancyModel
from .entities import VacancyEntity


class ORMVacancyConverter(BaseConverter):
    def handle(
        self,
        obj: VacancyModel | VacancyEntity,
    ) -> VacancyModel | VacancyEntity:
        """
        Handle given object and convert it to needed type
        Entity -> DTO
        DTO -> Entity
        """
        if obj.__class__ == VacancyModel:
            return self.convert_to_entity(obj)
        elif obj.__class__ == VacancyEntity:
            return self.convert_to_model(obj)
        else:
            raise IncorrectConverterArgument(
                choices=[VacancyModel.__name__, VacancyEntity.__name__]
            )

    def convert_to_entity(self, model: VacancyModel) -> VacancyEntity:
        """Convert Django model into entity"""
        candidates = model.interested_candidates.all()
        entity = VacancyEntity(
            id=model.id,
            employer=model.employer.to_entity(),
            interested_candidates=[cand.to_entity() for cand in candidates],
            title=model.title,
            description=model.description,
            company_name=model.company_name,
            is_remote=model.is_remote,
            required_experience=model.required_experience,
            location=model.location,
            required_skills=model.required_skills,
            updated_at=model.updated_at,
            created_at=model.created_at,
        )
        return entity

    def convert_to_model(self, entity: VacancyEntity) -> VacancyModel:
        """Convert entity into Django model"""
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
