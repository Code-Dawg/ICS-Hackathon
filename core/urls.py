"""
==============================================================================
ROOT URL ROUTER
Delegates requests to specific modular Django app routers.
==============================================================================
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
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
]
