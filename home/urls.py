from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('journey/', views.start_journey_view, name='start_journey'),
    path('reset/', views.reset_journey_view, name='reset_journey'),
    path('scenario/<int:order>/', views.scenario_detail_view, name='scenario_detail'),
    path('scenario/<int:order>/submit/', views.submit_choice_view, name='submit_choice'),
    path('explanation/<int:order>/', views.explanation_detail_view, name='explanation_detail'),
    path('report/', views.final_report_view, name='final_report'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
]