from src.apps.profiles.entities.profiles import (
    JobSeekerProfile as JobSeekerProfileEntity,
)
from src.apps.profiles.models.profiles import (
    JobSeekerProfile,
)
from src.common.converters.base import BaseConverter
from src.common.converters.exceptions import IncorrectConverterArgument


class ORMJobSeekerProfileConverter(BaseConverter):
    def handle(
        self,
        obj: JobSeekerProfileEntity | JobSeekerProfile
    ) -> JobSeekerProfileEntity | JobSeekerProfile:
        if obj.__class__ == JobSeekerProfileEntity:
            return self.convert_to_model(obj)
        elif obj.__class__ == JobSeekerProfile:
            return self.convert_to_entity(obj)
        else:
            raise IncorrectConverterArgument(
                obj=obj,
                choices=[
                    JobSeekerProfile.__name__,
                    JobSeekerProfileEntity.__name__,
                ]
            )

    def convert_to_entity(
        self, profile: JobSeekerProfile
    ) -> JobSeekerProfileEntity:
        return JobSeekerProfileEntity(
            id=profile.id,
            first_name=profile.first_name,
            last_name=profile.last_name,
            age=profile.age,
            email=profile.email,
            experience=profile.experience,
            skills=profile.skills,
            phone=profile.phone,
            about_me=profile.about_me,
        )

    def convert_to_model(
        self,
        profile: JobSeekerProfileEntity
    ) -> JobSeekerProfile:
        return JobSeekerProfile(
            id=profile.id,
            first_name=profile.first_name,
            last_name=profile.last_name,
            age=profile.age,
            email=profile.email,
            experience=profile.experience,
            skills=profile.skills,
            phone=profile.phone,
            about_me=profile.about_me,
        )
