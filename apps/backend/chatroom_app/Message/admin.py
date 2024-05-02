from django.contrib import admin
from .models import Massage

@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ['receiver', 'sender', 'text', 'date', 'see']
