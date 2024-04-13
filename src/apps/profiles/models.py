from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

from src.apps.users.models import CustomUser


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

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class JobSeekerProfile(BaseProfile):
    phone = models.CharField(
        max_length=25,
        blank=False,
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(limit_value=12),
            MaxValueValidator(limit_value=100),
        ]
    )
    about_me = models.TextField()
    experience = models.PositiveIntegerField(default=0)

    skills = ArrayField(
        models.CharField(max_length=30),
        blank=False,
    )

    class Meta:
        ordering = ('experience',)


class EmployerProfile(BaseProfile):
    ...
