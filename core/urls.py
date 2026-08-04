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
<<<<<<< HEAD
    path('accounts/register/', register, name='register'),
=======
    
    # Feature App Routers
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('footprints/', include('digitalfootprints.urls')),
    path('journey/', include('journey.urls')),
    path('quiz/', include('quiz.urls')),
    path('leaderboard/', include('leaderboard.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('statistics/', include('stats_app.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
>>>>>>> bc3b42e14bd05e092dc75e8019d6fe17608064bf
]
