"""
==============================================================================
STATISTICS MODELS
Stores global platform metrics (e.g. 100K+ Students, 2M+ Footprints).
==============================================================================
"""

from django.db import models

class GlobalStatistic(models.Model):
    key = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=100)
    value_number = models.IntegerField(default=0)
    suffix = models.CharField(max_length=10, default="+")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.label}: {self.value_number}{self.suffix}"
