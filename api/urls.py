from django.urls import path
from . import views

urlpatterns = [
    path('subjects', views.subjects, name ='subjects'),
    path('subjects/<str:subject_name>/', views.subject_tests, name="subjcet_tests")

]