from django.contrib import admin

from .models.vacancies import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'company_name',
        'open',
        'required_experience',
        'required_skills',
        'created_at',
    ]
