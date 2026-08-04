from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'privacy_score', 'footprint_risk', 'created_at')
    search_fields = ('user__username', 'user__email')
