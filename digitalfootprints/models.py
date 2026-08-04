"""
==============================================================================
DIGITAL FOOTPRINTS MODELS
Models representing footprint types: Positive, Negative, Passive, Active.
==============================================================================
"""

from django.db import models

class DigitalFootprintType(models.Model):
    CATEGORY_CHOICES = [
        ('positive', 'Positive Footprint'),
        ('negative', 'Negative Footprint'),
        ('passive', 'Passive Footprint'),
        ('active', 'Active Footprint'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default="fa-solid fa-fingerprint")
    tags = models.CharField(max_length=200, help_text="Comma-separated tags")

    def __str__(self):
        return f"{self.get_category_display()}: {self.title}"
