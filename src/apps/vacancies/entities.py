from dataclasses import dataclass, field
from datetime import datetime

from src.apps.profiles.entities.employers import EmployerEntity
from src.apps.profiles.entities.jobseekers import JobSeekerEntity


@dataclass
class VacancyEntity:
    id: int | None = field(default=None, kw_only=True)

    employer: EmployerEntity | None = field(kw_only=True, default=None)
    interested_candidates: list[JobSeekerEntity] = field(
        default_factory=list, kw_only=True,
    )

    title: str = ''
    description: str = ''
    location: str = ''
    company_name: str = ''
    salary: int = 0
    required_experience: int = 0
    updated_at: datetime | None = None
    is_remote: bool | None = None
    created_at: datetime = field(default_factory=datetime.now)
    required_skills: list[str] = field(default_factory=list)

    def to_dict(self, related: bool = False) -> dict:
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'company_name': self.company_name,
            'location': self.location,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'is_remote': self.is_remote,
            'required_experience': self.required_experience,
            'required_skills': self.required_skills,
        }
        if related:
            data['employer'] = self.employer.to_dict()
            data['interested_candidates'] = [
                candidate.to_dict() for candidate in self.interested_candidates
            ]
        return data
