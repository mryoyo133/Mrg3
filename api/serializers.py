from dataclasses import fields
from rest_framework import serializers
from .models import Score, User, Subject, Test, Question

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id','title']  


