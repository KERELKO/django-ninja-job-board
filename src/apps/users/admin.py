from django.contrib import admin

from .models import Favorite, CustomUser


admin.site.register(Favorite)
admin.site.register(CustomUser)
