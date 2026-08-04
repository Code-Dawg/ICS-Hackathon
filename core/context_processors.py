"""
==============================================================================
CORE CONTEXT PROCESSORS
Provides global data accessible across all templates automatically.
==============================================================================
"""

from django.conf import settings

def global_site_context(request):
    """
    Context processor to pass project-wide metadata and features to all templates.
    This allows base.html and partial templates to access global settings effortlessly.
    """
    return {
        'SITE_NAME': 'EduPulse',
        'SITE_TAGLINE': 'Futuristic Digital Footprint & Learning Platform',
        'CURRENT_YEAR': 2026,
    }
