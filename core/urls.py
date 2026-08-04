"""
==============================================================================
ROOT URL ROUTER
Delegates requests to specific modular Django app routers.
==============================================================================
"""

from django.contrib import admin
from django.urls import path

from home.views import home
from login.views import register

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/register/', register, name='register'),
]
