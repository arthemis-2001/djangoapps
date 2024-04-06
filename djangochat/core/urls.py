"""
Module containing URL patterns for mapping views to URLs.

URL Patterns:
- "" (empty string): Maps to the frontpage view
- "signup/": Maps to the signup view
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("signup/", views.signup, name="signup"),
]