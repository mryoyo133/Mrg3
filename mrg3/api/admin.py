from django.contrib import admin

from .models import Question, Score, Subject, Test, User, Answer

# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Score)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)