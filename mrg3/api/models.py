# Create your models here.

from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Subject(models.Model):
    name = models.CharField(max_length= 24)

    def __str__(self):
        return f'{self.name}'

class Score(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='+')
    user_score = models.PositiveIntegerField()

class Test(models.Model):
    title = models.CharField(max_length= 24, blank= True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null = True)
    score = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.title}'
    
class Question(models.Model):
    question_body = models.CharField(max_length=300)
    test = models.ForeignKey(Test, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.question_body}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_body = models.CharField(max_length=64)
    isCorrect = models.BooleanField()

    def __str__(self):
        return f'{self.question} : {self.answer_body}'