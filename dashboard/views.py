"""
==============================================================================
DASHBOARD VIEWS
Aggregates user profile, quiz attempts, and badges in a single dashboard view.
==============================================================================
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from quiz.models import QuizAttempt
from leaderboard.models import UserBadge

@login_required
def dashboard_view(request):
    """User personal dashboard."""
    profile, _ = Profile.objects.get_or_create(user=request.user)
    attempts = QuizAttempt.objects.filter(user=request.user).order_by('-completed_at')[:5]
    badges = UserBadge.objects.filter(user=request.user)

    context = {
        'profile': profile,
        'attempts': attempts,
        'badges': badges,
    }
    return render(request, 'dashboard/index.html', context)
