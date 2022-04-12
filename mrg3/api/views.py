from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subject, Test
from .serializer import SubjectSerializer, TestSerializer

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