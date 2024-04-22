from dataclasses import dataclass, field

from .base import BaseProfileEntity


@dataclass
class JobSeekerEntity(BaseProfileEntity):
    age: int
    phone: str
    about_me: str
    experience: int
    skills: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'age': self.age,
            'phone': self.phone,
            'about_me': self.about_me,
            'experience': self.experience,
            'skills': self.skills,
        }
