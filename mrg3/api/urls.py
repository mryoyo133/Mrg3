from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.subject, name='subject_api'),
    path('tests/<str:subject>',views.tests, name="test_api")
]
