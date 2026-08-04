from django.contrib import admin
from .models import PlayerProfile, Scenario, Choice, UserAnswer, Achievement, UserAchievement

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'situation_text', 'category')
    ordering = ('order',)
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('scenario', 'text', 'quality_type', 'score_impact')
    list_filter = ('quality_type', 'scenario__category')
    search_fields = ('text', 'explanation', 'consequences', 'tip')

@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_score', 'current_scenario_index', 'is_completed', 'created_at')
    list_filter = ('is_completed',)
    search_fields = ('user__username', 'user__email')

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'scenario', 'choice', 'score_delta', 'answered_at')
    list_filter = ('choice__quality_type', 'scenario__category')
    search_fields = ('user__username', 'scenario__title')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('icon_emoji', 'title', 'badge_code', 'criteria_type')
    search_fields = ('title', 'badge_code', 'description')

@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'unlocked_at')
    search_fields = ('user__username', 'achievement__title')

