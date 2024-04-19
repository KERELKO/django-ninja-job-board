from ninja import Schema


class BaseEmployerProfileSchema(Schema):
    first_name: str
    last_name: str
    email: str
    company_name: str = ''


class EmployerProfileOut(BaseEmployerProfileSchema):
    id: int


class EmployerProfileIn(BaseEmployerProfileSchema):
    user_id: int


class EmployerProfileUpdate(BaseEmployerProfileSchema):
    ...
