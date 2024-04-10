from uuid import uuid4

from django.utils import timezone
from django.db import models
from django.utils.text import slugify

from taggit.managers import TaggableManager

from src.apps.profiles.models import EmployerProfile, JobSeekerProfile
from src.core.utils.time import get_elapsed_time_with_message


class AvaiableManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return Vacancy.objects.filter(open=True)


class Vacancy(models.Model):
    # Relationships
    employer = models.ForeignKey(
        EmployerProfile,
        on_delete=models.CASCADE,
        related_name='vacancies',
    )
    interested = models.ManyToManyField(
        JobSeekerProfile,
        related_name='interested_in',
        blank=True,
    )
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
        blank=True,
        null=True
    )
    company_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    remote = models.BooleanField(
        blank=True,
        null=True,
    )
    required_experience = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
    )
    open = models.BooleanField(
        default=True,
        blank=True
    )
    # Managers
    required_skills = TaggableManager(
        verbose_name='required_skills'
    )
    objects = models.Manager()
    available = AvaiableManager()

    class Meta:
        ordering = ('created_at',)
        indexes = [
            models.Index(fields=['slug']),
        ]
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.slug:
            self.slug = slugify(str(lambda: uuid4()))
        return super().save(*args, **kwargs)

    def time_elapsed_since_creation(self) -> tuple[int, str, str]:
        '''
        Returns the elapsed time since creation,
        in tuple[int, str, str]:
            int - the elapsed time
            str - time unit
            str - message
        see utility 'get_elapsed_time_with_message'
        '''
        now = timezone.now()
        elapsed_time = now - self.created_at
        # Determine time unit based on elapsed time
        return get_elapsed_time_with_message(elapsed_time)
