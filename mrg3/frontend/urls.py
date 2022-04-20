from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index-frontend'),
    path('register/', views.register, name="register-frontend"),
    path("login/", views.login_view, name='login-frontend'),
    path("logout/", views.logout_view, name='logout-frontend')
]