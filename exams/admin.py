from django.contrib import admin
# from .models import Subject, Exam, Topic, Question, Grade
from .waec_model import WAEC, Questions, Subject, Year

# admin.site.register(Subject)
# admin.site.register(Exam)
# admin.site.register(Topic)
# admin.site.register(Question)
# admin.site.register(Grade)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'subject', 'year', 'answer')
    list_filter = ('subject', 'year')

admin.site.register(WAEC)
admin.site.register(Year)
admin.site.register(Subject)
admin.site.register(Questions, QuestionsAdmin)

