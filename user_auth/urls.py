"""
user_auth/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]
