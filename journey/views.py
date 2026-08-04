"""
==============================================================================
JOURNEY VIEWS
Implements the 12-level gamified learning journey state machine.
==============================================================================
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

# Pre-defined Levels with lessons and challenges for gamified progression
LEVELS_DATA = [
    {
        "level": 1,
        "title": "Create Account",
        "icon": "fa-user-plus",
        "description": "Establish your digital identity with cryptographic credentials.",
        "lesson": "<p>Welcome to <strong>Footprint Quest</strong>! Your digital footprint starts with the credentials you create.</p><p>By registering for an account, you create an intentional, secure anchor point for your digital identity, encrypted with industry-standard cryptographic hashing.</p>",
        "question": "Level 1 is completed automatically when you register and log in to the platform!",
        "choices": [],
        "correct": 0
    },
    {
        "level": 2,
        "title": "Welcome to Digital Footprints",
        "icon": "fa-door-open",
        "description": "Learn what a digital footprint is and how it is created.",
        "lesson": "<p>A <strong>digital footprint</strong> is the permanent trail of data you leave behind on the internet. This includes the websites you visit, the messages you send, the searches you perform, and the metadata tracked by servers.</p><p>Understanding your footprint is the first step toward reclaiming digital sovereignty.</p>",
        "question": "Which of the following constructs your digital footprint?",
        "choices": [
            "A. Only social media posts",
            "B. Searches, clicks, cookies, and network logs",
            "C. Only files you download"
        ],
        "correct": 1
    },
    {
        "level": 3,
        "title": "Active vs Passive Footprints",
        "icon": "fa-fingerprint",
        "description": "Understand the difference between active posts and silent background tracking.",
        "lesson": "<p>Your footprint is split into two categories:</p><ul><li><strong>Active:</strong> Data you post intentionally (emails, tweets, form submissions).</li><li><strong>Passive:</strong> Data collected without your active involvement (IP address, location tracking, browser fingerprinting, and search histories).</li></ul>",
        "question": "Which of the following is a PASSIVE digital footprint?",
        "choices": [
            "A. Writing a comment on a blog post",
            "B. A server logging your browser type and geographic location",
            "C. Uploading a photo to a cloud server"
        ],
        "correct": 1
    },
    {
        "level": 4,
        "title": "Positive vs Negative Footprints",
        "icon": "fa-scale-balanced",
        "description": "Learn how your footprint can help your career or leak private data.",
        "lesson": "<p>Footprints aren't always bad. A <strong>positive footprint</strong> is a curated online portfolio, open-source work, or professional profile. A <strong>negative footprint</strong> consists of leaked passwords, compromised accounts, or overshared personal details.</p>",
        "question": "How can a positive digital footprint benefit a professional?",
        "choices": [
            "A. By helping hackers target them with phishing attacks",
            "B. By showing hiring managers verified credentials and open-source contributions",
            "C. By making their real-time location public to everyone"
        ],
        "correct": 1
    },
    {
        "level": 5,
        "title": "Social Media Awareness",
        "icon": "fa-share-nodes",
        "description": "Over-sharing online is a key risk. Master settings and boundaries.",
        "lesson": "<p>Social media apps monetize your attention and personal details. Oversharing your location, birthday, school, or boarding passes gives social engineers the leverage to impersonate or hack you.</p><p>Always verify privacy settings and think twice before posting private milestones.</p>",
        "question": "What is the safest practice when posting online?",
        "choices": [
            "A. Leave all posts open to the public to build reach",
            "B. Keep accounts private and never post sensitive personal data like home addresses",
            "C. Post vacation photos in real-time showing your empty house"
        ],
        "correct": 1
    },
    {
        "level": 6,
        "title": "Password & Privacy",
        "icon": "fa-key",
        "description": "Create unhackable password strategies and multi-factor defense.",
        "lesson": "<p>Weak or recycled passwords are the leading cause of identity theft. Secure accounts with long passphrases (e.g. four random words), and always activate Multi-Factor Authentication (MFA) to prevent unauthorized entry.</p>",
        "question": "Which of the following password styles is the most secure?",
        "choices": [
            "A. P@ssword123!",
            "B. green-cow-jupiter-coffee-4",
            "C. MyName1998"
        ],
        "correct": 1
    },
    {
        "level": 7,
        "title": "Phishing Awareness",
        "icon": "fa-mask",
        "description": "Detect deceptive emails, links, and socially engineered attacks.",
        "lesson": "<p>Phishing attacks use deceptive emails and replica login pages to trick you into revealing passwords. Look closely at the domain name of senders, inspect links before clicking, and never submit login details on external request forms.</p>",
        "question": "You get an email from 'admin@verification-netflix.com' saying your card expired. What should you do?",
        "choices": [
            "A. Click the link and type your card info immediately",
            "B. Forward it to your friends to verify if it is real",
            "C. Delete it; verify your subscription status directly inside Netflix's official website"
        ],
        "correct": 2
    },
    {
        "level": 8,
        "title": "Digital Reputation",
        "icon": "fa-address-card",
        "description": "How schools, employers, and search engines view your online profile.",
        "lesson": "<p>Your online reputation is permanent. Once content is indexed by search engines or archived by the WayBack Machine, it is very difficult to purge. Keep your digital presence clean, respectful, and secure.</p>",
        "question": "Are deleted posts completely gone from the internet?",
        "choices": [
            "A. Yes, deleting a post removes all records worldwide",
            "B. No, third-party crawlers, screenshots, or archive caches may preserve it",
            "C. Yes, GDPR rules guarantee automatic global database deletion"
        ],
        "correct": 1
    },
    {
        "level": 9,
        "title": "Safe Browsing",
        "icon": "fa-globe",
        "description": "Using VPNs, Tor, HTTPS, and ad-blockers to shield your traffic.",
        "lesson": "<p>Websites track you using advertising pixels, browser canvas fingerprinting, and cookie synchronization. Minimize this trackability by browsing with secure protocols (HTTPS), tracker-blocking extensions, and virtual private networks (VPNs).</p>",
        "question": "What is the primary benefit of HTTPS encryption?",
        "choices": [
            "A. It secures data in transit between your browser and the server",
            "B. It deletes all cookies on your computer automatically",
            "C. It blocks all ads and trackers on search pages"
        ],
        "correct": 0
    },
    {
        "level": 10,
        "title": "Privacy Quiz",
        "icon": "fa-clipboard-question",
        "description": "Test your core knowledge of footprints, passwords, and threats.",
        "lesson": "<p>Let's check your understanding of core privacy engineering topics. Ensuring you know how tracking cookies, password managers, and data leaks operate keeps you safe online.</p>",
        "question": "Which browser setting is best to stop tracking by third-party data brokers?",
        "choices": [
            "A. Blocking third-party cookies and script execution permissions",
            "B. Clearing search history from your Google Account",
            "C. Setting window size to full screen"
        ],
        "correct": 0
    },
    {
        "level": 11,
        "title": "Final Challenge",
        "icon": "fa-trophy",
        "description": "A simulated live footprint auditing tool to clean up your shadow.",
        "lesson": "<p>A data breach leak occurs, compromising your email on a public forum. Your core task as a digital citizen is to audit your active footprints and rotate credentials immediately.</p>",
        "question": "If your login credentials leak in a third-party data breach, what is your first step?",
        "choices": [
            "A. Ignore it since the breach happened to someone else",
            "B. Update your password on the breached site and anywhere else you reused that password, then enable 2FA",
            "C. Delete your email account completely"
        ],
        "correct": 1
    },
    {
        "level": 12,
        "title": "Digital Footprint Report",
        "icon": "fa-file-signature",
        "description": "View your final digital sovereignty audit and export your certificate.",
        "lesson": "<p>Incredible work! You have finished all 12 levels of the Footprint Quest roadmap. You have mastered passwords, tracking vectors, phishing threats, reputation management, and security audits.</p><p>You are now a certified Privacy Sovereign!</p>",
        "question": "What is the core principle of digital sovereignty?",
        "choices": [
            "A. Disconnecting from the internet forever",
            "B. Taking proactive control of your personal data, credentials, and digital footprint",
            "C. Allowing tech platforms to manage your privacy settings by default"
        ],
        "correct": 1
    }
]

def journey_view(request):
    """Renders the gamified learning journey level-map page."""
    user = request.user
    
    # Calculate user's current level (default is 2 if logged in, or 1 if anonymous)
    if user.is_authenticated:
        # Get or create profile
        profile = getattr(user, 'profile', None)
        if not profile:
            from accounts.models import Profile
            profile = Profile.objects.create(user=user)
        
        # If user is logged in, Level 1 (Create Account) is completed, so they must be at least Level 2
        if profile.current_level < 2:
            profile.current_level = 2
            profile.save()
            
        current_user_level = profile.current_level
        xp = profile.xp
    else:
        current_user_level = 1
        xp = 0

    # Process level statuses
    processed_levels = []
    for lvl in LEVELS_DATA:
        level_num = lvl["level"]
        status = "locked"
        
        if level_num < current_user_level:
            status = "completed"
        elif level_num == current_user_level:
            status = "unlocked"
        else:
            status = "locked"
            
        processed_levels.append({
            "level": level_num,
            "title": lvl["title"],
            "icon": lvl["icon"],
            "description": lvl["description"],
            "status": status,
            "lesson": lvl["lesson"],
            "question": lvl["question"],
            "choices": lvl["choices"],
            "correct": lvl["correct"]
        })
        
    # Calculate completion percentage
    # Max completed level is current_user_level - 1. E.g. level 2 active means level 1 completed (1/12 = 8.33%)
    completed_count = min(current_user_level - 1, 12)
    progress_percentage = int((completed_count / 12) * 100)

    context = {
        'levels': processed_levels,
        'current_user_level': current_user_level,
        'user_xp': xp,
        'progress_percentage': progress_percentage
    }
    return render(request, 'journey/index.html', context)

@login_required
def complete_level_view(request):
    """AJAX endpoint to complete a level and unlock the next one."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            completed_level = int(data.get('level'))
            
            profile = request.user.profile
            
            # Verify the user is completing their current level
            if completed_level == profile.current_level:
                # Level up!
                profile.current_level += 1
                profile.xp += 100 # Award 100 XP per level
                profile.save()
                
                # Check if this unlocks next levels or finishes journey
                next_level = profile.current_level
                is_finished = next_level > 12
                
                return JsonResponse({
                    'status': 'success',
                    'message': f'Level {completed_level} Completed! +100 XP',
                    'xp': profile.xp,
                    'current_level': next_level,
                    'is_finished': is_finished
                })
            else:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid level completion attempt.'
                }, status=400)
                
        except (ValueError, TypeError, json.JSONDecodeError):
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid request format.'
            }, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Only POST method allowed.'}, status=405)
