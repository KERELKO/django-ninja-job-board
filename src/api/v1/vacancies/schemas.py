from datetime import datetime

from ninja import Field, Schema

from src.apps.vacancies.entities.vacancies import Vacancy as VacancyEntity


class BaseVacancySchema(Schema):
    title: str
    description: str
    company_name: str
    created_at: datetime
    required_skills: list[str] = Field(default_factory=list)
    remote: bool | None = None
    location: str | None = None
    required_experience: int = 0


class VacancyIn(BaseVacancySchema):
    ...


class VacancyOut(BaseVacancySchema):
    id: int

    @staticmethod
    def from_entity(entity: VacancyEntity) -> 'VacancyOut':
        return VacancyOut(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            company_name=entity.company_name,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            location=entity.location,
            required_experience=entity.required_experience,
            remote=entity.remote,
            required_skills=entity.required_skills,
        )
