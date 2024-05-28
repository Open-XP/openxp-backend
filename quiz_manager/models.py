from django.db import models
from django.conf import settings
from exams.waec_model import (
    WAEC, 
    Questions, 
    Subject, 
    Year
    )
from datetime import timezone
from datetime import timedelta

class TestInstance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='test_instances')
    exam = models.ForeignKey(WAEC, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Questions)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Test by {self.user} on {self.exam} - {self.subject.name} {self.year.year}"

    def mark_as_completed(self):
        self.is_completed = True
        self.end_time = timezone.now() 
        self.save()
        

class UserAnswer(models.Model):
    test_instance = models.ForeignKey(TestInstance, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1, choices=Questions.ANSWER_CHOICES, blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.selected_option:
            self.is_correct = self.selected_option == self.question.answer
        else:
            self.is_correct = False
        super(UserAnswer, self).save(*args, **kwargs)

    def __str__(self):
        correct_status = "correct" if self.is_correct else "incorrect"
        return f"Answer to {self.question.question} by {self.test_instance.user}: {correct_status}"

    
class UserScore(models.Model):
    score = models.IntegerField(null=True, blank=True)
    total_time = models.CharField(max_length=50, null=True, blank=True)
    test_instance = models.ForeignKey(TestInstance, on_delete=models.CASCADE, related_name='user_scores')
    correct_questions = models.ManyToManyField(Questions, related_name='correct_in_scores', blank=True)
    incorrect_questions = models.ManyToManyField(Questions, related_name='incorrect_in_scores', blank=True)

    def __str__(self):
        return f"Score for {self.test_instance}: {self.score}"

class TotalStudyTime(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    overall_study_time = models.DurationField(default=timedelta(seconds=0)) 
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Total study time for {self.user.username}: {self.overall_study_time}"