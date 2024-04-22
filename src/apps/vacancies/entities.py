from dataclasses import dataclass, field
from datetime import datetime

from src.apps.profiles.entities.employers import EmployerEntity
from src.apps.profiles.entities.jobseekers import JobSeekerEntity


@dataclass
class VacancyEntity:
    title: str
    description: str
    created_at: datetime
    id: int | None = None
    location: str = ''
    salary: int = 0
    company_name: str = ''
    employer: EmployerEntity | None = None
    updated_at: datetime | None = None
    is_remote: bool | None = None
    required_experience: int = 0
    interested_candidates: list[JobSeekerEntity] = field(default_factory=list)
    required_skills: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "employer": self.employer.to_dict(),
            "title": self.title,
            "description": self.description,
            "company_name": self.company_name,
            "location": self.location,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_remote": self.is_remote,
            "required_experience": self.required_experience,
            "interested_candidates": [
                candidate.to_dict() for candidate in self.interested_candidates
            ],
            "required_skills": self.required_skills
        }
