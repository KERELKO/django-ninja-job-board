from django.contrib import admin

from .models.jobseekers import JobSeekerProfile
from .models.employers import EmployerProfile


@admin.register(JobSeekerProfile)
class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name',
        'age', 'skills', 'experience', 'phone',
    ]


@admin.register(EmployerProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name',
    ]
