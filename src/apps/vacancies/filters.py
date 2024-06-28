from datetime import datetime

from pydantic import BaseModel, Field


class VacancyFilters(BaseModel):
    search: str = ''
    is_remote: bool | None = None
    required_experience__gte: int = 0
    created_at__gte: datetime | None = None
    required_skills: list[str] = Field(default_factory=list)
    location: str = ''
    company_name: str = ''
    salary__gte: int = 0
    salary__lte: int = 0
