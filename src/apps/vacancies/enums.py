from enum import Enum

from src.apps.profiles.entities.jobseekers import JobSeekerEntity
from src.apps.vacancies.entities import VacancyEntity


class VacancyCriteria(Enum):
    REQUIRED_EXPERIENCE_SCORE: float = 7.0
    INCR_IF_EXPERIENCE_HIGHER: bool = True
    SKILL_IN_SCORE: float = 2.0
    SKILL_NOT_IN_SCORE: float = 0.5

    @classmethod
    def calculate_score_from_experience(
        cls,
        candidate_experience: int,
        vacancy_required_experience: int,
    ) -> float:
        score = 0
        if candidate_experience >= vacancy_required_experience:
            score = cls.REQUIRED_EXPERIENCE_SCORE.value
            if cls.INCR_IF_EXPERIENCE_HIGHER.value:
                score += (
                    candidate_experience - vacancy_required_experience
                )
        return score

    @classmethod
    def calculate_score_from_skills(
        cls,
        candidate_skills: list[str],
        vacancy_required_skills: list[str],
    ) -> float:
        score = 0
        for skill in candidate_skills:
            if skill in vacancy_required_skills:
                score += cls.SKILL_IN_SCORE.value
            else:
                score += cls.SKILL_NOT_IN_SCORE.value
        return score

    @classmethod
    def get_candidate_rating(
        cls,
        candidate: JobSeekerEntity,
        vacancy: VacancyEntity,
    ) -> float:
        rating = 0
        rating += cls.calculate_score_from_skills(
            candidate_skills=candidate.skills,
            vacancy_required_skills=vacancy.required_skills,
        )
        rating += cls.calculate_score_from_experience(
            candidate_experience=candidate.experience,
            vacancy_required_experience=vacancy.required_experience,
        )
        return rating
