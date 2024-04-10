from django.contrib import admin

from .models import JobSeekerProfile, EmployerProfile


admin.site.register(JobSeekerProfile)
admin.site.register(EmployerProfile)
