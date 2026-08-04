"""
==============================================================================
JOURNEY MODELS
Represents steps in the interactive digital footprint learning roadmap.
==============================================================================
"""

from django.db import models

class JourneyStep(models.Model):
    step_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default="fa-solid fa-route")

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"
