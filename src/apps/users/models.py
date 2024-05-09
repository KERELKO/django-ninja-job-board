from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class CustomUser(AbstractUser): ...


class Favorite(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name='favorites',
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(
        ContentType,
        related_name='%(class)s_related',
        on_delete=models.CASCADE,
        limit_choices_to={
            'model__in': (
                'jobseekerprofile',
                'vacancy',
            ),
        },
    )
    object_id = models.PositiveIntegerField()
    favorite = GenericForeignKey('content_type', 'object_id')
