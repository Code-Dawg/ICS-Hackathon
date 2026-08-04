"""
==============================================================================
JOURNEY URL ROUTER
==============================================================================
"""

from django.urls import path
from . import views

app_name = 'journey'

urlpatterns = [
    path('', views.journey_view, name='index'),
    path('level-data/<int:level_id>/', views.get_level_data_view, name='get_level_data'),
    path('submit/', views.submit_level_completion_view, name='submit_completion'),
    path('report/', views.final_report_view, name='report'),
]
