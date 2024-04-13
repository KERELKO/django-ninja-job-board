from datetime import datetime
from pydantic import BaseModel, Field


class VacancyFilters(BaseModel):
    search: str | None = None
    remote: bool | None = None
    required_experience__gte: int = 0
    created_at__gte: datetime | None = None
    required_skills: list[str] = Field(default_factory=list)
    location: str | None = None
    company_name: str | None = None
