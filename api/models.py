# Create your models here.

from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    scores = models.ManyToManyField('Score')

class Subject(models.Model):
    name = models.CharField(max_length= 24)

    def __str__(self):
        return f'{self.name}'

class Score(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    score = models.CharField(blank=True, max_length= 2)

class Test(models.Model):
    title = models.CharField(max_length= 24, blank= True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null = True)
    questions = models.ManyToManyField('Question')
    def __str__(self):
        return f'{self.title}'
    
class Question(models.Model):
    question_body = models.CharField(max_length=300)
    choice_1 = models.CharField(max_length=64, blank=True)
    choice_2 = models.CharField(max_length=64, blank=True)
    choice_3 = models.CharField(max_length=64, blank=True)
    choice_4 = models.CharField(max_length=64, blank=True)
    answer =  models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f'{self.question_body}'

