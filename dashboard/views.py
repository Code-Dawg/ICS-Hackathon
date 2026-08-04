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
    """Show a learner's progress alongside the global XP standings."""
    profile, _ = Profile.objects.get_or_create(user=request.user)
    attempts = QuizAttempt.objects.filter(user=request.user).order_by('-completed_at')[:5]
    badges = UserBadge.objects.filter(user=request.user)
    rankings = list(Profile.objects.select_related('user').order_by('-xp', 'user__username'))
    user_rank = next(
        (index for index, player in enumerate(rankings, start=1) if player.user_id == request.user.id),
        None,
    )
    completed_levels = min(max(profile.current_level - 1, 0), 12)

    context = {
        'profile': profile,
        'attempts': attempts,
        'badges': badges,
        'rankings': rankings,
        'user_rank': user_rank,
        'progress_percentage': int((completed_levels / 12) * 100),
    }
    return render(request, 'dashboard/index.html', context)
