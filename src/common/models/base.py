from datetime import timezone
from django.db import models

from src.common.utils.time import get_elapsed_time_with_message


class TimedBaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='DateTimeField, sets when object is created',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='DateTimeField, updates for every object update',
    )

    class Meta:
        abstract = True

    def time_elapsed_since_creation(self) -> tuple[int, str, str]:
        """
        Returns the elapsed time since creation,
        in tuple[int, str, str]:
            int - the elapsed time
            str - time unit
            str - message
        see utility 'get_elapsed_time_with_message'
        """
        now = timezone.now()
        elapsed_time = now - self.created_at
        # Determine time unit based on elapsed time
        return get_elapsed_time_with_message(elapsed_time)
