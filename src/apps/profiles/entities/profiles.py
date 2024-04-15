from abc import abstractmethod
from dataclasses import dataclass, field


@dataclass
class BaseProfile:
    id: int
    first_name: str
    last_name: str
    email: str

    @abstractmethod
    def to_dict(self) -> dict:
        ...


@dataclass
class JobSeekerProfile(BaseProfile):
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


@dataclass
class EmployerProfile(BaseProfile):

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }
