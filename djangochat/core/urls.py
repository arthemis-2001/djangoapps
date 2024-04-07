"""
Module containing URL patterns for mapping views to URLs.

URL Patterns:
- "" (empty string): Maps to the frontpage view
- "signup/": Maps to the signup view
"""
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
