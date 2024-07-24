from datetime import datetime

from ninja import Field, Schema
from pydantic import ConfigDict

from src.api.v1.profiles.employers.schemas import EmployerProfileOut
from src.api.v1.profiles.jobseekers.schemas import JobSeekerProfileOut
from src.apps.vacancies.entities import VacancyEntity


class VacancyIn(Schema):
    employer_id: int
    title: str
    description: str
    company_name: str
    created_at: datetime
    salary: int = 0
    required_skills: list[str] = Field(default_factory=list)
    is_remote: bool | None = None
    location: str | None = None
    required_experience: int = 0


class VacancyOut(Schema):
    id: int
    employer: EmployerProfileOut
    interested_candidates: list[JobSeekerProfileOut] = Field(
        default_factory=list
    )
    title: str
    description: str
    company_name: str
    created_at: datetime
    salary: int = 0
    required_skills: list[str] = Field(default_factory=list)
    is_remote: bool | None = None
    location: str | None = None
    required_experience: int = 0

    @staticmethod
    def from_entity(entity: VacancyEntity) -> 'VacancyOut':
        return VacancyOut(**entity.to_dict(related=True))


class VacancyUpdate(Schema):
    model_config = ConfigDict(extra='forbid')
    title: str
    description: str
    company_name: str
    created_at: datetime
    salary: int = 0
    required_skills: list[str] = Field(default_factory=list)
    is_remote: bool | None = None
    location: str | None = None
    required_experience: int = 0
