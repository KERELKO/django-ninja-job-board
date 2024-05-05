from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

from src.apps.profiles.entities.jobseekers import JobSeekerEntity

from .base import BaseProfile


class JobSeekerProfile(BaseProfile):
    phone = models.CharField(
        max_length=25,
        blank=False,
    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(limit_value=18),
            MaxValueValidator(limit_value=100),
        ]
    )
    about_me = models.TextField()
    experience = models.PositiveIntegerField(
        default=0,
    )
    skills = ArrayField(
        models.CharField(max_length=30),
        blank=False,
    )
    allow_notifications = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ('-first_name',)

    def save(self, *args, **kwargs):
        self.skills = [skill.lower() for skill in self.skills]
        return super().save(*args, **kwargs)

    def to_entity(self) -> JobSeekerEntity:
        return JobSeekerEntity(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            age=self.age,
            about_me=self.about_me,
            experience=self.experience,
            skills=self.skills,
            phone=self.phone,
        )
