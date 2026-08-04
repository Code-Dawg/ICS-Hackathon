"""
==============================================================================
JOURNEY VIEWS
Implements the 20-level gamified progression backend and scoring models.
==============================================================================
"""

import json
from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import transaction

from accounts.models import Profile
from .models import JourneyStep, UserLevelProgress, Achievement, UserAchievement
from .scenarios import SCENARIOS

# Definitions of all 20 levels in the Footprint Quest adventure
LEVELS_METADATA = [
    {"level": 1, "title": "Create Account", "icon": "fa-user-plus", "type": "auth", "desc": "Establish your cryptographic profile and begin your quest."},
    {"level": 2, "title": "First Steps Online", "icon": "fa-shoe-prints", "type": "scenario", "desc": "Navigate notifications, downloads, terms, and library terminals."},
    {"level": 3, "title": "Your First Social Media Account", "icon": "fa-share-nodes", "type": "scenario", "desc": "Manage profile visibility, request filters, and viral surveys."},
    {"level": 4, "title": "Active vs Passive Digital Footprints", "icon": "fa-fingerprint", "type": "scenario", "desc": "Decouple query tracking, location telemetry, and browser fingerprints."},
    {"level": 5, "title": "Sharing Photos", "icon": "fa-camera", "type": "scenario", "desc": "Manage photo EXIF metadata, barcode leaks, and key duplicate images."},
    {"level": 6, "title": "Strong Passwords", "icon": "fa-key", "type": "game_password", "desc": "Drag characters together and build a strong passphrase."},
    {"level": 7, "title": "Public Wi-Fi", "icon": "fa-wifi", "type": "game_wifi", "desc": "Quick sorting game to determine safe vs unsafe hotspots."},
    {"level": 8, "title": "Online Shopping", "icon": "fa-cart-shopping", "type": "scenario", "desc": "Inspect discount sites, text delivery scams, and transaction cards."},
    {"level": 9, "title": "Fake Websites", "icon": "fa-circle-xmark", "type": "game_scam", "desc": "Spot suspicious domains and spelling parameters."},
    {"level": 10, "title": "Phishing Emails", "icon": "fa-envelope-open-text", "type": "game_phish", "desc": "Identify red-flag header details in replica mail setups."},
    {"level": 11, "title": "Privacy Settings", "icon": "fa-sliders", "type": "game_settings", "desc": "Configure safety toggles for browser security configurations."},
    {"level": 12, "title": "Browser Cookies", "icon": "fa-cookie", "type": "game_cookie", "desc": "Feed the Cookie Monster by sorting tracking cookies from standard ones."},
    {"level": 13, "title": "App Permissions", "icon": "fa-mobile-screen", "type": "game_permission", "desc": "Grant or deny hardware requests for specific application modules."},
    {"level": 14, "title": "Online Gaming Safety", "icon": "fa-gamepad", "type": "scenario", "desc": "Verify trade links, lobby voice chats, and administrator rights."},
    {"level": 15, "title": "Digital Reputation", "icon": "fa-address-card", "type": "scenario", "desc": "Manage deletion archives, search indexes, and community alignments."},
    {"level": 16, "title": "Cyberbullying", "icon": "fa-circle-exclamation", "type": "scenario", "desc": "Document harassment logs, keyword auto-filters, and support structures."},
    {"level": 17, "title": "Data Brokers", "icon": "fa-database", "type": "scenario", "desc": "Submit opt-out requests to data brokers and sweepstakes directories."},
    {"level": 18, "title": "Search Engines", "icon": "fa-magnifying-glass", "type": "scenario", "desc": "Inspect search filter bubbles and personal search query lists."},
    {"level": 19, "title": "Password Managers", "icon": "fa-vault", "type": "game_match", "desc": "Match password concepts and security cards."},
    {"level": 20, "title": "Final Cyber Challenge", "icon": "fa-trophy", "type": "game_escape", "desc": "Complete the Cyber Escape Room to obtain certification."}
]

# Badge seed template
BADGES_SEED = [
    {"code": "bronze_explorer", "name": "Bronze Explorer", "desc": "Complete 5 levels of the quest.", "icon": "fa-solid fa-compass", "xp_reward": 50},
    {"code": "silver_explorer", "name": "Silver Explorer", "desc": "Complete 10 levels of the quest.", "icon": "fa-solid fa-map", "xp_reward": 100},
    {"code": "gold_explorer", "name": "Gold Explorer", "desc": "Complete 18 levels of the quest.", "icon": "fa-solid fa-chess-knight", "xp_reward": 150},
    {"code": "privacy_rookie", "name": "Privacy Rookie", "desc": "Reach a Privacy Score of 90 or above.", "icon": "fa-solid fa-user-shield", "xp_reward": 50},
    {"code": "cyber_guardian", "name": "Cyber Guardian", "desc": "Reach a Security Score of 90 or above.", "icon": "fa-solid fa-shield-halved", "xp_reward": 80},
    {"code": "footprint_master", "name": "Footprint Master", "desc": "Reach a Reputation Score of 90 or above.", "icon": "fa-solid fa-fingerprint", "xp_reward": 100},
    {"code": "password_hero", "name": "Password Hero", "desc": "Complete Level 6 (Strong Passwords) with high accuracy.", "icon": "fa-solid fa-key", "xp_reward": 50},
    {"code": "scam_detector", "name": "Scam Detector", "desc": "Complete the Fake Websites and Phishing levels.", "icon": "fa-solid fa-eye-slash", "xp_reward": 80},
    {"code": "safe_browser", "name": "Safe Browser", "desc": "Complete Level 12 and Level 13 successfully.", "icon": "fa-solid fa-globe", "xp_reward": 80},
    {"code": "digital_citizen", "name": "Digital Citizen", "desc": "Accumulate 200 or more gold coins.", "icon": "fa-solid fa-coins", "xp_reward": 100},
    {"code": "privacy_legend", "name": "Privacy Legend", "desc": "Complete Level 20 with all metrics > 90.", "icon": "fa-solid fa-crown", "xp_reward": 200}
]

def seed_badges():
    """Helper to populate default achievements/badges into DB."""
    for badge in BADGES_SEED:
        Achievement.objects.get_or_create(
            code=badge["code"],
            defaults={
                "name": badge["name"],
                "description": badge["desc"],
                "icon_class": badge["icon"],
                "xp_reward": badge["xp_reward"]
            }
        )

def update_streaks(profile):
    """Calculates active daily logins and streak multipliers."""
    today = date.today()
    if profile.last_active_date == today:
        return  # Streak already validated today
    
    if profile.last_active_date == today - timedelta(days=1):
        profile.current_streak += 1
    else:
        profile.current_streak = 1  # Streak broken, reset
        
    profile.longest_streak = max(profile.longest_streak, profile.current_streak)
    profile.last_active_date = today
    profile.save()

def check_badge_unlocks(user):
    """Iterates through badge conditions to auto-unlock achievements."""
    profile = user.profile
    seed_badges()
    unlocked_badges = []
    
    completed_levels = UserLevelProgress.objects.filter(user=user).count()
    
    # Define checklist maps
    badge_checks = [
        ("bronze_explorer", completed_levels >= 5),
        ("silver_explorer", completed_levels >= 10),
        ("gold_explorer", completed_levels >= 18),
        ("privacy_rookie", profile.privacy_score >= 90),
        ("cyber_guardian", profile.security_score >= 90),
        ("footprint_master", profile.reputation_score >= 90),
        ("digital_citizen", profile.coins >= 200),
        ("password_hero", UserLevelProgress.objects.filter(user=user, level_number=6).exists()),
        ("scam_detector", UserLevelProgress.objects.filter(user=user, level_number=9).exists() and UserLevelProgress.objects.filter(user=user, level_number=10).exists()),
        ("safe_browser", UserLevelProgress.objects.filter(user=user, level_number=12).exists() and UserLevelProgress.objects.filter(user=user, level_number=13).exists()),
        ("privacy_legend", UserLevelProgress.objects.filter(user=user, level_number=20).exists() and profile.privacy_score >= 90 and profile.security_score >= 90)
    ]
    
    for code, condition in badge_checks:
        if condition:
            ach = Achievement.objects.filter(code=code).first()
            if ach:
                ua, created = UserAchievement.objects.get_or_create(user=user, achievement=ach)
                if created:
                    profile.xp += ach.xp_reward
                    profile.save()
                    unlocked_badges.append(ach.name)
                    
    return unlocked_badges

def journey_view(request):
    """Renders the gamified learning adventure level-map page."""
    user = request.user
    seed_badges()
    
    if user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=user)
        update_streaks(profile)
        
        # If logged in, Level 1 (Create Account) is auto-completed
        if profile.current_level < 2:
            profile.current_level = 2
            profile.save()
            
        current_user_level = profile.current_level
        xp = profile.xp
        coins = profile.coins
        stars = profile.stars
        streak = profile.current_streak
    else:
        current_user_level = 1
        xp = 0
        coins = 0
        stars = 0
        streak = 0

    processed_levels = []
    for lvl in LEVELS_METADATA:
        level_num = lvl["level"]
        
        # Check if they have already completed this level in UserLevelProgress
        has_progress = False
        if user.is_authenticated:
            has_progress = UserLevelProgress.objects.filter(user=user, level_number=level_num).exists()
            
        if level_num < current_user_level or has_progress:
            status = "completed"
        else:
            status = "unlocked"
            
        processed_levels.append({
            "level": level_num,
            "title": lvl["title"],
            "icon": lvl["icon"],
            "type": lvl["type"],
            "description": lvl["desc"],
            "status": status
        })

    completed_count = min(current_user_level - 1, 20)
    progress_percentage = int((completed_count / 20) * 100)

    context = {
        'levels': processed_levels,
        'current_user_level': current_user_level,
        'user_xp': xp,
        'user_coins': coins,
        'user_stars': stars,
        'user_streak': streak,
        'progress_percentage': progress_percentage
    }
    return render(request, 'journey/index.html', context)

@login_required
def get_level_data_view(request, level_id):
    """AJAX endpoint providing questions/metadata for a selected level."""
    level_id = int(level_id)
    lvl_meta = next((l for l in LEVELS_METADATA if l["level"] == level_id), None)
    if not lvl_meta:
        return JsonResponse({"status": "error", "message": "Level not found."}, status=404)
        
    # All levels are open/unlocked
    profile = request.user.profile

    response_data = {
        "level": level_id,
        "title": lvl_meta["title"],
        "type": lvl_meta["type"],
        "description": lvl_meta["desc"],
        "icon": lvl_meta["icon"],
        "scenarios": []
    }
    
    # Include scenario data if applicable
    if lvl_meta["type"] == "scenario":
        scenarios_list = SCENARIOS.get(level_id, [])
        # Send full list for this level
        for sc in scenarios_list:
            response_data["scenarios"].append({
                "id": sc["id"],
                "story": sc["story"],
                "choices": sc["choices"],
                "correct_idx": sc["correct_idx"],
                "feedback": sc["feedback"]
            })
            
    # Mini-games will supply custom configurations or challenges
    elif lvl_meta["type"] == "game_escape":
        # Final puzzle details
        response_data["scenarios"] = SCENARIOS.get(level_id, [])[:4] # Core escape scenarios

    return JsonResponse(response_data)

@login_required
def submit_level_completion_view(request):
    """AJAX endpoint validating score logs, updating profile and rewards."""
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Only POST method allowed.'}, status=405)
        
    try:
        data = json.loads(request.body)
        level = int(data.get('level'))
        xp_earned = int(data.get('xp', 50))
        coins_earned = int(data.get('coins', 10))
        stars_earned = int(data.get('stars', 1))
        correct_count = int(data.get('correct_count', 0))
        wrong_count = int(data.get('wrong_count', 0))
        
        # Adjustments to metrics
        privacy_diff = int(data.get('privacy_diff', 0))
        security_diff = int(data.get('security_diff', 0))
        reputation_diff = int(data.get('reputation_diff', 0))
        trust_diff = int(data.get('trust_diff', 0))
        
        profile = request.user.profile
        # All levels are open/unlocked
        if level < 1 or level > 20:
            return JsonResponse({'status': 'error', 'message': 'Invalid level number.'}, status=400)
            
        with transaction.atomic():
            # Update Progression - only advance if completing current or higher level
            if level >= profile.current_level:
                profile.current_level = level + 1
            profile.xp += xp_earned
            profile.coins += coins_earned
            profile.stars += stars_earned
            
            # Counter metrics
            profile.correct_answers += correct_count
            profile.wrong_answers += wrong_count
            
            # Clamp scores between 0 and 100
            profile.privacy_score = max(0, min(100, profile.privacy_score + privacy_diff))
            profile.security_score = max(0, min(100, profile.security_score + security_diff))
            profile.reputation_score = max(0, min(100, profile.reputation_score + reputation_diff))
            profile.trust_score = max(0, min(100, profile.trust_score + trust_diff))
            
            # Calculate Knowledge score based on correct answers
            total_answered = profile.correct_answers + profile.wrong_answers
            if total_answered > 0:
                profile.knowledge_score = int((profile.correct_answers / total_answered) * 100)
                
            # Recalculate Risk rating based on average of Privacy and Security
            avg_score = (profile.privacy_score + profile.security_score) / 2
            if avg_score >= 85:
                profile.footprint_risk = 'Low'
            elif avg_score >= 60:
                profile.footprint_risk = 'Medium'
            else:
                profile.footprint_risk = 'High'
                
            profile.save()
            
            # Log Level completion progress
            UserLevelProgress.objects.get_or_create(
                user=request.user,
                level_number=level,
                defaults={"score": correct_count * 10}
            )
            
            # Check for Badge achievements
            unlocked_badges = check_badge_unlocks(request.user)
            
            return JsonResponse({
                'status': 'success',
                'message': f'Level {level} completed!',
                'xp': profile.xp,
                'coins': profile.coins,
                'stars': profile.stars,
                'current_level': profile.current_level,
                'unlocked_badges': unlocked_badges,
                'is_finished': profile.current_level > 20
            })
            
    except (ValueError, TypeError, json.JSONDecodeError) as e:
        return JsonResponse({'status': 'error', 'message': f'Invalid payload: {str(e)}'}, status=400)

@login_required
def final_report_view(request):
    """Aggregates all score logs, calculations, and generates final metrics."""
    profile = request.user.profile
    seed_badges()
    
    # Calculate grades
    def get_grade(score):
        if score >= 90: return 'A'
        if score >= 80: return 'B'
        if score >= 70: return 'C'
        if score >= 60: return 'D'
        return 'F'
        
    privacy_grade = get_grade(profile.privacy_score)
    security_grade = get_grade(profile.security_score)
    reputation_grade = get_grade(profile.reputation_score)
    trust_grade = get_grade(profile.trust_score)
    
    # Overall footprint score is the average of scores
    overall_score = int((profile.privacy_score + profile.security_score + profile.reputation_score + profile.trust_score) / 4)
    
    # Badge details
    user_badges = UserAchievement.objects.filter(user=request.user).select_related('achievement')
    badges_unlocked = [ub.achievement for ub in user_badges]
    
    # Timeline
    timeline_completions = UserLevelProgress.objects.filter(user=request.user).order_by('level_number')
    
    # Dynamic skill suggestions
    skills_analysis = []
    
    if profile.privacy_score < 80:
        skills_analysis.append({
            "name": "Metadata & Browsing Privacy",
            "status": "Weak",
            "color": "var(--accent-magenta)",
            "tip": "Limit cookies, block tracking scripts with adblockers, and disable background EXIF tracking on photo devices."
        })
    else:
        skills_analysis.append({
            "name": "Metadata & Browsing Privacy",
            "status": "Strong",
            "color": "var(--accent-emerald)",
            "tip": "Excellent cookie auditing and search safety parameters."
        })
        
    if profile.security_score < 80:
        skills_analysis.append({
            "name": "Cyber Defense & Passphrases",
            "status": "Weak",
            "color": "var(--accent-magenta)",
            "tip": "Rotate shared passwords, generate long passphrases, and activate Multi-Factor Authentication on core portals."
        })
    else:
        skills_analysis.append({
            "name": "Cyber Defense & Passphrases",
            "status": "Strong",
            "color": "var(--accent-emerald)",
            "tip": "Highly robust phishing analysis and passphrase entropy."
        })
        
    if profile.reputation_score < 80:
        skills_analysis.append({
            "name": "Digital Reputation Management",
            "status": "Weak",
            "color": "var(--accent-magenta)",
            "tip": "Check search caches, delete old comments, and audit what tags friends associate with your handles."
        })
    else:
        skills_analysis.append({
            "name": "Digital Reputation Management",
            "status": "Strong",
            "color": "var(--accent-emerald)",
            "tip": "Great digital record hygiene and community interactions."
        })

    context = {
        'profile': profile,
        'overall_score': overall_score,
        'overall_grade': get_grade(overall_score),
        'privacy_grade': privacy_grade,
        'security_grade': security_grade,
        'reputation_grade': reputation_grade,
        'trust_grade': trust_grade,
        'badges': badges_unlocked,
        'timeline': timeline_completions,
        'skills': skills_analysis,
        'total_levels_completed': timeline_completions.count()
    }
    return render(request, 'journey/report.html', context)
