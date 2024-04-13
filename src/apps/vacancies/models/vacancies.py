from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField

from src.common.models.base import TimedBaseModel


class AvaiableManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return Vacancy.objects.filter(open=True)


class Vacancy(TimedBaseModel):
    # Fields
    title = models.CharField(
        max_length=300
    )
    description = models.TextField(
        blank=False
    )
    slug = models.SlugField(
        blank=True,
        null=False,
        unique_for_date='created_at',
    )
    location = models.CharField(
        max_length=255,
    )
    company_name = models.CharField(
        max_length=255,
    )
    remote = models.BooleanField(
        blank=True,
        null=True,
    )
    required_experience = models.PositiveIntegerField(
        blank=True,
        default=0,
    )
    open = models.BooleanField(
        default=True,
    )
    required_skills = ArrayField(
        models.CharField(max_length=30),
        blank=False,
    )
    # Managers
    objects = models.Manager()
    available = AvaiableManager()

    class Meta:
        ordering = (
            'created_at',
        )
        indexes = (
            models.Index(fields=['slug']),
        )
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.slug:
            self.slug = self.id
        return super().save(*args, **kwargs)
