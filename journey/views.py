"""
==============================================================================
JOURNEY VIEWS
==============================================================================
"""

from django.shortcuts import render
from .models import JourneyStep

def journey_view(request):
    """Renders the learning journey timeline page."""
    steps = JourneyStep.objects.all()
    return render(request, 'journey/index.html', {'steps': steps})
