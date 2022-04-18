from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('subjects', views.subject, name='subject_api'),
    path('tests/<str:subject>',views.tests, name="tests_api"),
    path("test/<str:test>", views.test, name = "test-api"),
    path('answers/<int:question_id>', views.answer, name="answer-api"),
    path("questions/<str:test>", views.questions, name="questions-api"),
    path("submit", views.test_submit, name= 'submit-api'),
    path("scores", views.get_scores, name='score-api')
]
