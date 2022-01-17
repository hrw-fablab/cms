from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FablabUser

admin.site.register(FablabUser, UserAdmin)
