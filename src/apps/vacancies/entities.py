from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Vacancy:
    id: int
    title: str
    description: str
    company_name: str
    slug: str
    location: str
    created_at: datetime
    open: bool = True
    updated_at: datetime | None = None
    remote: bool | None = None
    required_experience: int = 0
    required_skills: list[str] = field(default_factory=list)
