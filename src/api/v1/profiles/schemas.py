from ninja import Schema, Field


class JobSeekerProfileOut(Schema):
    first_name: str
    last_name: str
    age: int
    phone: str
    skills: list[str] = Field(default_factory=list)
    about_me: str


class EmployerProfileOut(Schema):
    first_name: str
    last_name: str
