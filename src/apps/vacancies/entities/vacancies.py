from dataclasses import dataclass, field
from datetime import datetime

from src.apps.profiles.entities.profiles import (
    JobSeekerProfile,
    EmployerProfile,
)


@dataclass
class Vacancy:
    id: int
    employer: EmployerProfile
    title: str
    description: str
    company_name: str
    location: str
    created_at: datetime
    updated_at: datetime | None = None
    is_remote: bool | None = None
    required_experience: int = 0
    interested_candidates: list[JobSeekerProfile] = field(default_factory=list)
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
