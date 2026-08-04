from django.contrib import admin
from .models import DigitalFootprintType

@admin.register(DigitalFootprintType)
class DigitalFootprintTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'tags')
    list_filter = ('category',)
