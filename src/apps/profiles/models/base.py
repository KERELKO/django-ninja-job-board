from abc import abstractmethod

from django.db import models

from src.apps.users.models import CustomUser
from src.apps.profiles.entities.base import BaseProfileEntity


class BaseProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        related_name='%(class)s_related',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=250
    )
    last_name = models.CharField(
        max_length=250
    )
    email = models.CharField(
        max_length=60,
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @abstractmethod
    def to_entity(self) -> BaseProfileEntity:
        ...
