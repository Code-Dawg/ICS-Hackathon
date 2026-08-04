from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from .models import PlayerProfile, Scenario, Choice, UserAnswer, Achievement, UserAchievement
from .forms import UserRegistrationForm

def home_view(request):
    """
    Landing page with overview of Digital Footprint game.
    """
    total_scenarios = Scenario.objects.count()
    context = {
        'total_scenarios': total_scenarios,
    }
    if request.user.is_authenticated:
        profile, created = PlayerProfile.objects.get_or_create(user=request.user)
        context['profile'] = profile
    return render(request, 'home.html', context)


def register_view(request):
    """
    User registration view. Automatically initializes PlayerProfile upon successful registration.
    """
    if request.user.is_authenticated:
        return redirect('start_journey')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            PlayerProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, f"Welcome aboard, {user.username}! Your Digital Footprint journey begins now.")
            return redirect('start_journey')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def start_journey_view(request):
    """
    Entry point for starting or resuming the game journey.
    """
    profile, _ = PlayerProfile.objects.get_or_create(user=request.user)
    
    # If completed or index out of range, redirect to final report
    total_scenarios = Scenario.objects.count()
    if profile.is_completed or profile.current_scenario_index > total_scenarios:
        return redirect('final_report')

    return redirect('scenario_detail', order=profile.current_scenario_index)


@login_required
def reset_journey_view(request):
    """
    Resets user's progress and score so they can replay the game journey.
    """
    if request.method == 'POST':
        profile, _ = PlayerProfile.objects.get_or_create(user=request.user)
        profile.current_score = 0
        profile.current_scenario_index = 1
        profile.is_completed = False
        profile.save()

        # Clear answers and achievements for fresh run
        UserAnswer.objects.filter(user=request.user).delete()
        UserAchievement.objects.filter(user=request.user).delete()

        messages.info(request, "Your journey has been reset! Good luck achieving a higher score.")
        return redirect('scenario_detail', order=1)
    
    return redirect('start_journey')


@login_required
def scenario_detail_view(request, order):
    """
    Displays a specific scenario for the user to make a choice.
    """
    profile, _ = PlayerProfile.objects.get_or_create(user=request.user)
    total_scenarios = Scenario.objects.count()

    scenario = get_object_or_404(Scenario, order=order)
    choices = scenario.choices.all()

    # Check if user already answered this scenario
    existing_answer = UserAnswer.objects.filter(user=request.user, scenario=scenario).first()

    progress_pct = int((order / total_scenarios) * 100) if total_scenarios > 0 else 0

    context = {
        'profile': profile,
        'scenario': scenario,
        'choices': choices,
        'order': order,
        'total_scenarios': total_scenarios,
        'progress_pct': progress_pct,
        'existing_answer': existing_answer,
    }
    return render(request, 'scenario.html', context)


@login_required
def submit_choice_view(request, order):
    """
    Processes choice submission, updates score, records answer, checks achievements,
    and redirects to explanation view.
    """
    if request.method != 'POST':
        return redirect('scenario_detail', order=order)

    choice_id = request.POST.get('choice_id')
    if not choice_id:
        messages.error(request, "Please select an answer before submitting.")
        return redirect('scenario_detail', order=order)

    scenario = get_object_or_404(Scenario, order=order)
    choice = get_object_or_404(Choice, id=choice_id, scenario=scenario)
    profile, _ = PlayerProfile.objects.get_or_create(user=request.user)

    # Save or update UserAnswer
    user_answer, created = UserAnswer.objects.get_or_create(
        user=request.user,
        scenario=scenario,
        defaults={'choice': choice, 'score_delta': choice.score_impact}
    )
    if not created:
        user_answer.choice = choice
        user_answer.score_delta = choice.score_impact
        user_answer.save()

    # Recalculate total score
    total_score = UserAnswer.objects.filter(user=request.user).aggregate(models.Sum('score_delta'))['score_delta__sum'] or 0
    profile.current_score = total_score

    # Advance current_scenario_index if higher
    total_scenarios = Scenario.objects.count()
    if order >= profile.current_scenario_index:
        profile.current_scenario_index = order + 1

    if order >= total_scenarios:
        profile.is_completed = True

    profile.save()

    # Evaluate Achievements
    check_and_award_achievements(request.user, profile, order, total_scenarios)

    return redirect('explanation_detail', order=order)


def check_and_award_achievements(user, profile, current_order, total_scenarios):
    """
    Helper function to check and unlock badges for the user.
    """
    unlocked_new = []

    # 1. FIRST_STEP
    if current_order >= 1:
        ach = Achievement.objects.filter(badge_code='FIRST_STEP').first()
        if ach and not UserAchievement.objects.filter(user=user, achievement=ach).exists():
            UserAchievement.objects.create(user=user, achievement=ach)

    # 2. PRIVACY_GUARDIAN (Score 50+)
    if profile.current_score >= 50:
        ach = Achievement.objects.filter(badge_code='PRIVACY_GUARDIAN').first()
        if ach and not UserAchievement.objects.filter(user=user, achievement=ach).exists():
            UserAchievement.objects.create(user=user, achievement=ach)

    # 3. FOOTPRINT_MASTER (Score 150+)
    if profile.current_score >= 150:
        ach = Achievement.objects.filter(badge_code='FOOTPRINT_MASTER').first()
        if ach and not UserAchievement.objects.filter(user=user, achievement=ach).exists():
            UserAchievement.objects.create(user=user, achievement=ach)

    # 4. CAUTIOUS_COMMUNICATOR (5 consecutive safe decisions)
    last_5_answers = UserAnswer.objects.filter(user=user).order_by('-scenario__order')[:5]
    if len(last_5_answers) == 5:
        all_safe = all(ans.choice.quality_type in ['EXCELLENT', 'GOOD'] for ans in last_5_answers)
        if all_safe:
            ach = Achievement.objects.filter(badge_code='CAUTIOUS_COMMUNICATOR').first()
            if ach and not UserAchievement.objects.filter(user=user, achievement=ach).exists():
                UserAchievement.objects.create(user=user, achievement=ach)

    # 5. DIGITAL_CITIZEN (Completed all)
    if profile.is_completed:
        ach = Achievement.objects.filter(badge_code='DIGITAL_CITIZEN').first()
        if ach and not UserAchievement.objects.filter(user=user, achievement=ach).exists():
            UserAchievement.objects.create(user=user, achievement=ach)


@login_required
def explanation_detail_view(request, order):
    """
    Renders the educational explanation screen after an answer is submitted.
    """
    profile, _ = PlayerProfile.objects.get_or_create(user=request.user)
    scenario = get_object_or_404(Scenario, order=order)
    user_answer = get_object_or_404(UserAnswer, user=request.user, scenario=scenario)

    total_scenarios = Scenario.objects.count()
    next_order = order + 1 if order < total_scenarios else None
    progress_pct = int((order / total_scenarios) * 100) if total_scenarios > 0 else 0

    # Fetch user achievements unlocked so far
    user_achievements = UserAchievement.objects.filter(user=request.user).select_related('achievement')

    context = {
        'profile': profile,
        'scenario': scenario,
        'user_answer': user_answer,
        'choice': user_answer.choice,
        'order': order,
        'total_scenarios': total_scenarios,
        'next_order': next_order,
        'progress_pct': progress_pct,
        'user_achievements': user_achievements,
    }
    return render(request, 'explanation.html', context)


@login_required
def final_report_view(request):
    """
    Generates the comprehensive final Digital Footprint Report with rating, stats,
    strengths, areas for improvement, recommendations, and full decision timeline.
    """
    profile, _ = PlayerProfile.objects.get_or_create(user=request.user)
    answers = UserAnswer.objects.filter(user=request.user).select_related('scenario', 'choice').order_by('scenario__order')

    if not answers.exists():
        messages.warning(request, "Please start the journey to generate your Digital Footprint Report.")
        return redirect('start_journey')

    total_completed = answers.count()
    final_score = profile.current_score

    # Breakdown statistics
    positive_choices = answers.filter(choice__quality_type__in=['EXCELLENT', 'GOOD']).count()
    safe_choices = answers.filter(choice__quality_type='EXCELLENT').count()
    risky_choices = answers.filter(choice__quality_type__in=['RISKY', 'DANGEROUS']).count()
    good_decisions_pct = round((positive_choices / total_completed * 100), 1) if total_completed > 0 else 0

    # Overall Rating Logic
    if final_score >= 180 or good_decisions_pct >= 85:
        rating = "Excellent Digital Citizen"
        rating_badge = "👑"
        rating_color = "success"
        rating_desc = "Outstanding performance! You proactively manage your digital footprint, safeguard privacy, and model responsible online behavior."
    elif final_score >= 110 or good_decisions_pct >= 65:
        rating = "Responsible User"
        rating_badge = "🛡️"
        rating_color = "primary"
        rating_desc = "Good digital citizenship! You consistently make safe decisions, with just a few areas where your footprint can be tightened."
    elif final_score >= 40 or good_decisions_pct >= 45:
        rating = "Needs Improvement"
        rating_badge = "⚠️"
        rating_color = "warning"
        rating_desc = "Proceed with caution. Several choices exposed your personal data, location, or reputation to unnecessary digital risks."
    else:
        rating = "High Digital Risk"
        rating_badge = "🚨"
        rating_color = "danger"
        rating_desc = "High digital risk! Your online decisions leave vulnerable search trails, exposed location data, and reputational hazards."

    # Analyze Strengths & Areas for Improvement by Scenario Category
    category_performance = {}
    for ans in answers:
        cat = ans.scenario.category
        if cat not in category_performance:
            category_performance[cat] = {'safe': 0, 'risky': 0, 'tips': []}
        
        if ans.choice.quality_type in ['EXCELLENT', 'GOOD']:
            category_performance[cat]['safe'] += 1
        else:
            category_performance[cat]['risky'] += 1
            category_performance[cat]['tips'].append(ans.choice.tip)

    strengths = [cat for cat, data in category_performance.items() if data['safe'] > data['risky']]
    areas_for_improvement = [cat for cat, data in category_performance.items() if data['risky'] >= data['safe']]

    # Personalized Recommendations
    recommendations = []
    for cat, data in category_performance.items():
        if data['tips']:
            recommendations.extend(data['tips'][:2]) # Pick key tips from risky choices

    # Fallback default tips if user was perfect
    if not recommendations:
        recommendations = [
            "Conduct an annual digital footprint audit by searching your name on major search engines.",
            "Regularly review profile privacy settings across all personal social media platforms.",
            "Keep work/school accounts separate from casual gaming and personal handles."
        ]

    # User unlocked achievements
    user_achievements = UserAchievement.objects.filter(user=request.user).select_related('achievement')

    context = {
        'profile': profile,
        'answers': answers,
        'total_completed': total_completed,
        'final_score': final_score,
        'positive_choices': positive_choices,
        'safe_choices': safe_choices,
        'risky_choices': risky_choices,
        'good_decisions_pct': good_decisions_pct,
        'rating': rating,
        'rating_badge': rating_badge,
        'rating_color': rating_color,
        'rating_desc': rating_desc,
        'strengths': strengths,
        'areas_for_improvement': areas_for_improvement,
        'recommendations': recommendations,
        'user_achievements': user_achievements,
    }
    return render(request, 'final_report.html', context)


@login_required
def leaderboard_view(request):
    """
    Community Scoreboard showing top Digital Footprint scores.
    """
    top_profiles = PlayerProfile.objects.select_related('user').order_by('-current_score', '-current_scenario_index')[:20]
    return render(request, 'leaderboard.html', {'top_profiles': top_profiles})

