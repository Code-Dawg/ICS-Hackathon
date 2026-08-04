"""
==============================================================================
JOURNEY MODELS
Represents level progress, achievements, and badges for learners.
==============================================================================
"""

from django.db import models
from django.contrib.auth.models import User

class JourneyStep(models.Model):
    step_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default="fa-solid fa-route")

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"

class UserLevelProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='level_progress')
    level_number = models.IntegerField()
    score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'level_number')
        ordering = ['level_number']

    def __str__(self):
        return f"{self.user.username} -> Level {self.level_number} (score: {self.score})"

class Achievement(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default="fa-solid fa-medal")
    xp_reward = models.IntegerField(default=50)

    def __str__(self):
        return self.name

class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')

    def __str__(self):
        return f"{self.user.username} unlocked {self.achievement.name}"
