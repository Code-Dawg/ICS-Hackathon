from django.contrib import admin
from .models import ContactMessage, FAQItem

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_at', 'is_resolved')
    list_filter = ('is_resolved',)

@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_featured')
