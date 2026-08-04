from django.db import models
from django.contrib.auth.models import User

class PlayerProfile(models.Model):
    """
    Tracks player progress, cumulative score, and completion status.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    current_score = models.IntegerField(default=0)
    current_scenario_index = models.IntegerField(default=1, help_text="Current scenario order number user is on")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile (Score: {self.current_score})"


class Scenario(models.Model):
    """
    Represents an educational digital footprint situation/scenario.
    """
    order = models.PositiveIntegerField(unique=True, help_text="Sequence order of scenario (1, 2, 3...)")
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, help_text="Category e.g. Social Media, Permanent Records, Privacy")
    situation_text = models.TextField(help_text="Short real-life situation description")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Scenario {self.order}: {self.title}"


class Choice(models.Model):
    """
    A decision option for a scenario with digital footprint impact & feedback.
    """
    QUALITY_CHOICES = [
        ('EXCELLENT', 'Excellent Choice'),
        ('GOOD', 'Good Choice'),
        ('NEUTRAL', 'Neutral Choice'),
        ('RISKY', 'Risky Choice'),
        ('DANGEROUS', 'Dangerous Choice'),
    ]

    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255, help_text="Text shown to the user")
    score_impact = models.IntegerField(help_text="Score change e.g. +10, +5, 0, -5, -10")
    quality_type = models.CharField(max_length=20, choices=QUALITY_CHOICES, default='GOOD')
    explanation = models.TextField(help_text="Why this choice affects your digital footprint")
    consequences = models.TextField(help_text="Long-term consequences of this choice")
    tip = models.TextField(help_text="Actionable tip for safer digital footprint management")

    def __str__(self):
        return f"Choice ({self.quality_type}, {self.score_impact:+d} pts): {self.text[:40]}"


class UserAnswer(models.Model):
    """
    Records a user's answer to a specific scenario during their journey.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    score_delta = models.IntegerField()
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'scenario')
        ordering = ['scenario__order']

    def __str__(self):
        return f"{self.user.username} answered Scenario {self.scenario.order} -> {self.choice.quality_type}"


class Achievement(models.Model):
    """
    Badge or achievement unlocked by achieving specific milestones.
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    icon_emoji = models.CharField(max_length=10, default='🏆')
    badge_code = models.CharField(max_length=50, unique=True)
    criteria_type = models.CharField(max_length=50, help_text="e.g. FIRST_STEP, SAFE_STREAK, HIGH_SCORE, MASTER")

    def __str__(self):
        return f"{self.icon_emoji} {self.title}"


class UserAchievement(models.Model):
    """
    Tracks which user has unlocked which achievement.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')

    def __str__(self):
        return f"{self.user.username} unlocked {self.achievement.title}"

