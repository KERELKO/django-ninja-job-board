from pydantic import BaseModel, Field


class JobSeekerFilters(BaseModel):
    skills: list[str] = Field(default_factory=list)
    age__gte: int = 18
    experience__gte: int = 0
    vacancy_id: int = 0
    allow_notifications: bool = False


class EmployerFilter(BaseModel):
    company_name: str = ''
