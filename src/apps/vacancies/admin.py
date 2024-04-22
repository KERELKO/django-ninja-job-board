from django.contrib import admin

from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'company_name',
        'open',
        'required_experience',
        'required_skills',
        'created_at',
    ]
