from ninja import Schema, Field

from src.apps.profiles.entities.jobseekers import JobSeekerEntity


class BaseJobSeekerProfileSchema(Schema):
    first_name: str
    last_name: str
    age: int = 0
    about_me: str
    phone: str = ''
    experience: int = 0
    skills: list[str]
    allow_notifications: bool = False


class JobSeekerProfileIn(BaseJobSeekerProfileSchema):
    user_id: int


class JobSeekerProfileUpdate(BaseJobSeekerProfileSchema):
    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    about_me: str | None = None
    phone: str | None = None
    experience: int | None = None
    skills: list[str] = Field(default_factory=list)
    allow_notifications: bool | None = None


class JobSeekerProfileOut(BaseJobSeekerProfileSchema):
    id: int

    @staticmethod
    def from_entity(entity: JobSeekerEntity) -> 'JobSeekerProfileOut':
        return JobSeekerProfileOut(**entity.to_dict())
