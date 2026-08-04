"""
==============================================================================
ACCOUNTS MODELS
Extends User model with Profile info, Privacy Score, & Footprint Risk metrics.
==============================================================================
"""

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, default="Passionate learner exploring digital privacy.")
    privacy_score = models.IntegerField(default=85, help_text="Score out of 100")
    footprint_risk = models.CharField(max_length=20, default="Low", choices=[
        ('Low', 'Low Risk'),
        ('Medium', 'Medium Risk'),
        ('High', 'High Risk')
    ])
    avatar_url = models.URLField(blank=True, default="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
