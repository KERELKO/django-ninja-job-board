from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField

from src.apps.profiles.models.jobseekers import JobSeekerProfile
from src.apps.profiles.models.employers import EmployerProfile
from src.common.models.base import TimedBaseModel


class AvaiableManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return Vacancy.objects.filter(open=True)


class Vacancy(TimedBaseModel):
    # Relationships
    employer = models.ForeignKey(
        EmployerProfile,
        on_delete=models.CASCADE,
        related_name='vacancies',
    )
    interested_candidates = models.ManyToManyField(
        JobSeekerProfile,
        related_name='interested_in',
        blank=True,
    )
    # Fields
    title = models.CharField(
        max_length=300,
    )
    description = models.TextField(
        blank=False,
    )
    salary = models.PositiveIntegerField(
        default=0,
        blank=True,
    )
    location = models.CharField(
        max_length=255,
        default='',
        blank=True,
    )
    company_name = models.CharField(
        max_length=255,
        blank=True,
        default='',
    )
    is_remote = models.BooleanField(
        blank=True,
        null=True,
    )
    required_experience = models.PositiveIntegerField(
        blank=True,
        default=0,
    )
    required_skills = ArrayField(
        models.CharField(max_length=30),
        blank=False,
    )
    # Other fields
    open = models.BooleanField(
        default=True,
    )
    slug = models.SlugField(
        blank=True,
        null=False,
        unique_for_date='created_at',
    )
    # Managers
    objects = models.Manager()
    available = AvaiableManager()

    class Meta:
        ordering = ('created_at',)
        indexes = (models.Index(fields=['slug']),)
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.slug:
            self.slug = self.id
        self.required_skills = [
            skill.lower() for skill in self.required_skills
        ]
        return super().save(*args, **kwargs)
