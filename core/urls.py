"""
==============================================================================
ROOT URL ROUTER
Delegates requests to specific modular Django app routers.
==============================================================================
"""

from django.contrib import admin
<<<<<<< HEAD
from django.urls import path

from home.views import home
from login import views
=======
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> f7df1f8d166cd8acd3a2dbc44289b82f08c394f9

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('accounts/register/', views.register, name='register'),
]
    
=======
    
    # Feature App Routers
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('footprints/', include('digitalfootprints.urls')),
    path('journey/', include('journey.urls')),
    path('quiz/', include('quiz.urls')),
    path('leaderboard/', include('leaderboard.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('statistics/', include('statistics.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> f7df1f8d166cd8acd3a2dbc44289b82f08c394f9
