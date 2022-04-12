from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubjectsSerializer, TestSerializer
from .models import Subject, Test

# Create your views here.
@api_view(['GET'])
def subjects(request):
    subjects = Subject.objects.all()
    serializer = SubjectsSerializer(subjects, many = True)
    return Response(serializer.data)

@api_view(["GET"])
def subject_tests(request, subject_name):
    subject = Subject.objects.get(name = subject_name)
    tests = Test.objects.filter(subject = subject)
    serializer = TestSerializer(tests, many = True)
    return Response(serializer)
