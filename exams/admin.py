from django.contrib import admin
from .models import Subject, Exam, Topic, Question, Grade

admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Grade)
