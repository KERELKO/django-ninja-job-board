from datetime import datetime

from ninja import Field, Schema
from pydantic import ConfigDict

from src.apps.vacancies.entities.vacancies import Vacancy as VacancyEntity
from src.api.v1.profiles.jobseekers.schemas import JobSeekerProfileOut
from src.api.v1.profiles.employers.schemas import EmployerProfileOut


class BaseVacancySchema(Schema):
    title: str
    description: str
    company_name: str
    created_at: datetime
    salary: int = 0
    required_skills: list[str] = Field(default_factory=list)
    is_remote: bool | None = None
    location: str | None = None
    required_experience: int = 0


class VacancyIn(BaseVacancySchema):
    employer_id: int


class VacancyOut(BaseVacancySchema):
    id: int
    employer: EmployerProfileOut
    interested_candidates: list[JobSeekerProfileOut] = Field(
        default_factory=list
    )

    @staticmethod
    def from_entity(entity: VacancyEntity) -> 'VacancyOut':
        return VacancyOut(**entity.to_dict())


class VacancyUpdate(BaseVacancySchema):
    model_config = ConfigDict(extra='forbid')
