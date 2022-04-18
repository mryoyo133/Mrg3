from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Answer, Subject, Test, Question, Score
from .serializer import AnswerSerializer, QuestionSerializer, ScoreSerializer, SubjectSerializer, TestSerializer





# Create your views here.
@api_view(["GET"])
def subject(request):
    subject = Subject.objects.all()
    serializer = SubjectSerializer(subject, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def tests(request, subject):
    subject_id = Subject.objects.get(name = subject)
    test = Test.objects.filter(subject = subject_id)
    serializer = TestSerializer(test, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def test(request, test):
    test = Test.objects.get(title = test)
    result = TestSerializer(test)
    return Response(result.data)

@api_view(["GET"])
def questions(request, test):
    test = Test.objects.get(title = test)
    questions = Question.objects.filter(test = test)
    result = QuestionSerializer(questions, many = True)
    return Response(result.data)

@api_view(['GET'])
def answer(request, question_id):
    question = Question.objects.get(id = question_id)
    answers = Answer.objects.filter(question = question)
    serializer = AnswerSerializer(answers, many = True)
    return Response(serializer.data)


@api_view(['POST'])    
def test_submit(request):
    serializer = ScoreSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

@api_view(['GET'])
def get_scores(request):
    score = Score.objects.filter(student = request.user)
    serializer = ScoreSerializer(score, many = True)
    return Response(serializer.data)