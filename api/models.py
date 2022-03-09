# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    tests = models.ManyToManyField('Test')

class Subject(models.Model):
    name = models.CharField(max_length= 24)
    tests = models.ManyToManyField('Test', blank = True)

    def __str__(self):
        return f'{self.name}'

class Test(models.Model):
    title = models.CharField(max_length= 24, blank= True)
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

