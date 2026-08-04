"""
==============================================================================
DIGITAL FOOTPRINTS URL ROUTER
==============================================================================
"""

from django.urls import path
from . import views

app_name = 'digitalfootprints'

urlpatterns = [
    path('', views.footprint_list_view, name='index'),
]
