from django.contrib import admin
from .models import UserAnswer, TestInstance, UserScore, TotalStudyTime


admin.site.register(UserAnswer)
admin.site.register(TestInstance)
admin.site.register(UserScore)
admin.site.register(TotalStudyTime)

