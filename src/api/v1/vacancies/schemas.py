from datetime import datetime

from ninja import Schema

from src.apps.vacancies.entities.vacancies import Vacancy as VacancyEntity


class BaseVacancySchema(Schema):
    title: str
    description: str
    company_name: str
    created_at: datetime
    remote: bool | None = None
    location: str | None = None
    required_experience: int = 0


class VacancyIn(BaseVacancySchema):
    id: int
    slug: str | None = None
    open: bool = True


class VacancyOut(BaseVacancySchema):
    id: int
    slug: str
    open: bool

    @staticmethod
    def from_entity(entity: VacancyEntity) -> 'VacancyOut':
        return VacancyOut(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            slug=entity.slug,
            open=entity.open,
            company_name=entity.company_name,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            location=entity.location,
            required_experience=entity.required_experience,
            remote=entity.remote,
        )
