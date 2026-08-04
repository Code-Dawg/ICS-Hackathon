"""
==============================================================================
CORE CONTEXT PROCESSORS - FOOTPRINT QUEST
Provides global Footprint Quest metadata across all templates.
==============================================================================
"""

def global_site_context(request):
    return {
        'SITE_NAME': 'Footprint Quest',
        'SITE_TAGLINE': 'Gamified Digital Footprint & Privacy Quest',
        'CURRENT_YEAR': 2026,
    }
