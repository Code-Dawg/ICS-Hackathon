"""
==============================================================================
CONTACT URL ROUTER
==============================================================================
"""

from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact_view, name='index'),
    path('faq/', views.faq_view, name='faq'),
]
