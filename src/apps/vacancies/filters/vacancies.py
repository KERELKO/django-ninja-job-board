from pydantic import BaseModel, Field


class VacancyFilters(BaseModel):
    search: str | None = None
    required_skills: list[str] = Field(default_factory=list)
    required_experience: int = 0
    remote: bool | None = None
