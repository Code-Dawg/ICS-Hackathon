from django.contrib import admin
from .models import GlobalStatistic

@admin.register(GlobalStatistic)
class GlobalStatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'value_number', 'suffix', 'is_active')
