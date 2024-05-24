from dataclasses import dataclass

from .base import BaseProfileEntity


@dataclass
class EmployerEntity(BaseProfileEntity):
    company_name: str | None = None

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'company_name': self.company_name,
        }
