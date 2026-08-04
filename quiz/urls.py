"""
==============================================================================
QUIZ URL ROUTER
==============================================================================
"""

from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list_view, name='index'),
    path('<int:quiz_id>/', views.quiz_detail_view, name='detail'),
]
