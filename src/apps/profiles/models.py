from src.apps.users.models import CustomUser
from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    user = models.OneToOneField(
        CustomUser,
        related_name='profile',
        on_delete=models.CASCADE
    )
