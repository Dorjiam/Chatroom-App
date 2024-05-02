from django.contrib import admin
from .models import User

@admin.register(User)
class MassageAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'last_name', 'email', 'password', 'age']