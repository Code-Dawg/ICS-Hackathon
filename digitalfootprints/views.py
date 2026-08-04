"""
==============================================================================
DIGITAL FOOTPRINTS VIEWS
==============================================================================
"""

from django.shortcuts import render
from .models import DigitalFootprintType

def footprint_list_view(request):
    """Displays footprint categories and explanations."""
    footprints = DigitalFootprintType.objects.all()
    return render(request, 'digitalfootprints/index.html', {'footprints': footprints})
