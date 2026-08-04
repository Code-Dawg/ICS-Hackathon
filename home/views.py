"""
==============================================================================
HOME VIEWS
Renders the main futuristic landing page assembling all feature teasers.
==============================================================================
"""

from django.shortcuts import render

def home_view(request):
    """Main landing page entry point."""
    return render(request, 'home/index.html')
