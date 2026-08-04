"""
==============================================================================
STATISTICS URL ROUTER
==============================================================================
"""

from django.urls import path
from . import views

app_name = 'statistics'

urlpatterns = [
    path('', views.statistics_view, name='index'),
    path('api/', views.stats_api_view, name='api'),
]
