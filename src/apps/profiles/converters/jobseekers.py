from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.profiles.models.jobseekers import JobSeekerProfile
from src.common.converters.base import BaseConverter
from src.common.converters.exceptions import IncorrectConverterArgument


class ORMJobSeekerConverter(BaseConverter):
    def handle(
        self,
        obj: JobSeekerEntity | JobSeekerProfile
    ) -> JobSeekerEntity | JobSeekerProfile:
        if obj.__class__ == JobSeekerEntity:
            return self.convert_to_model(obj)
        elif obj.__class__ == JobSeekerProfile:
            return self.convert_to_entity(obj)
        else:
            raise IncorrectConverterArgument(
                obj=obj,
                choices=[
                    JobSeekerProfile.__name__,
                    JobSeekerEntity.__name__,
                ]
            )

    def convert_to_entity(
        self, profile: JobSeekerProfile
    ) -> JobSeekerEntity:
        return JobSeekerEntity(
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
        profile: JobSeekerEntity
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
