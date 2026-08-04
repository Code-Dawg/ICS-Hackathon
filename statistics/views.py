"""
==============================================================================
STATISTICS VIEWS
Provides HTML template analytics page & JSON endpoint for counter animations.
==============================================================================
"""

from django.shortcuts import render
from django.http import JsonResponse
from .models import GlobalStatistic

def statistics_view(request):
    """Renders analytics page."""
    stats = GlobalStatistic.objects.filter(is_active=True)
    return render(request, 'statistics/index.html', {'stats': stats})

def stats_api_view(request):
    """JSON API endpoint returning current platform counters."""
    stats = GlobalStatistic.objects.filter(is_active=True)
    data = [{
        'key': s.key,
        'label': s.label,
        'number': s.value_number,
        'suffix': s.suffix
    } for s in stats]
    return JsonResponse({'status': 'success', 'stats': data})
