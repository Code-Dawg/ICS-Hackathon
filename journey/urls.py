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
]
