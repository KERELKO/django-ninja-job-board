from datetime import datetime

from ninja import Field, Schema

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
    remote: bool | None = None
    location: str | None = None
    required_experience: int = 0


class VacancyIn(BaseVacancySchema):
    employer: EmployerProfileOut


class VacancyOut(BaseVacancySchema):
    id: int
    employer: EmployerProfileOut
    interested_candidates: list[JobSeekerProfileOut] = Field(
        default_factory=list
    )

    @staticmethod
    def from_entity(entity: VacancyEntity) -> 'VacancyOut':
        return VacancyOut(**entity.to_dict())


right_vacancy_data = {
  "data": {
    "items": [
      {
        "id": 1,
        "title": "Python Backend Developer",
        "description": (
            "We are looking for an"
            "experienced Python developer to join our team..."
        ),
        "company_name": "Atlantis",
        "created_at": "2024-04-14T07:13:01Z",
        "required_skills": ["Python", "Django", "RESTful API"],
        "is_remote": False,
        "location": "Vinnitsa",
        "required_experience": 1,
        "employer": {
          "id": 1,
          "name": "Atlantis Inc.",
          "website": "https://www.atlantis.com"
        },
        "interested_candidates": [
          {
            "id": 1,
            "name": "John Doe",
            "profile_url": "https://example.com/profile/johndoe"
          }
        ]
      }
    ],
    "pagination": {
      "offset": 0,
      "limit": 20,
      "total": 1
    }
  },
  "meta": {},
  "errors": []
}
