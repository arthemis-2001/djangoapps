from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.portfolio_list, name="portfolio_list"),
    path("portfolio/<int:pk>/", views.portfolio_detail, name="portfolio_detail"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", views.register, name="register"),
    path("portfolio/<int:pk>/like/", views.portfolio_like, name="portfolio_like")
]
