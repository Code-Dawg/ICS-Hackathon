from django.contrib import admin
from .models import JourneyStep

@admin.register(JourneyStep)
class JourneyStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title')
    ordering = ('step_number',)
