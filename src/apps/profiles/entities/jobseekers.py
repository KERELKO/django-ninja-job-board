from dataclasses import dataclass, field

from .base import BaseProfileEntity


@dataclass
class JobSeekerEntity(BaseProfileEntity):
    age: int | None = None
    phone: str | None = None
    about_me: str | None = None
    experience: int | None = None
    skills: list[str] = field(default_factory=list)
    allow_notifications: bool = False

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
            'allow_notifications': self.allow_notifications,
        }
