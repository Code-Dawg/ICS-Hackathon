"""
==============================================================================
ACCOUNTS MODELS
Extends User model with Profile info, rich gamified gameplay stats, & streaks.
==============================================================================
"""

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, default="Passionate learner exploring digital privacy.")
    
    # Gameplay Scores
    privacy_score = models.IntegerField(default=85, help_text="Score out of 100")
    security_score = models.IntegerField(default=85, help_text="Score out of 100")
    reputation_score = models.IntegerField(default=85, help_text="Score out of 100")
    trust_score = models.IntegerField(default=85, help_text="Score out of 100")
    knowledge_score = models.IntegerField(default=0, help_text="Score out of 100")
    
    footprint_risk = models.CharField(max_length=20, default="Low", choices=[
        ('Low', 'Low Risk'),
        ('Medium', 'Medium Risk'),
        ('High', 'High Risk')
    ])
    
    # Currencies and Progression
    current_level = models.IntegerField(default=2, help_text="Current active level (1 to 20)")
    xp = models.IntegerField(default=0, help_text="Experience points earned")
    coins = models.IntegerField(default=0, help_text="In-game gold coins")
    stars = models.IntegerField(default=0, help_text="Stars representing perfect level scores")
    
    # Counters and Streaks
    correct_answers = models.IntegerField(default=0)
    wrong_answers = models.IntegerField(default=0)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_active_date = models.DateField(null=True, blank=True)
    
    avatar_url = models.URLField(blank=True, default="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
