from django.contrib import admin
from .models import User, Subject, Test, Question
# Register your models here.

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(Question)
