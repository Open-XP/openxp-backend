from django.db import models
from django.conf import settings

from django.db import models

class ExamScheduler(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    exam_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.subject} - {self.date} - {self.exam_type}"