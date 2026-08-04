"""
==============================================================================
LEADERBOARD VIEWS
Renders top student rankings based on privacy scores and quiz attempts.
==============================================================================
"""

from django.shortcuts import render
from accounts.models import Profile

def leaderboard_view(request):
    """Global scoreboard ranking learners by earned XP."""
    top_profiles = Profile.objects.select_related('user').order_by('-xp', 'user__username')[:20]
    return render(request, 'leaderboard/index.html', {'profiles': top_profiles})
