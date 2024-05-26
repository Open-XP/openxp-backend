from django.db import models
from datetime import timedelta


class WAEC(models.Model):
    duration = models.DurationField(default=timedelta(minutes=60))
    total_questions = models.IntegerField(default=60, )
    
    class Meta:
        verbose_name = "WAEC Exam"
        verbose_name_plural = "WAEC Exams"
        
    def __str__(self):
        return "WAEC Exam"


class Year(models.Model):
    year = models.IntegerField(default=2010)

    def __str__(self):
        return str(self.year)


class Subject(models.Model):
    exam = models.ForeignKey(WAEC, related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


class Questions(models.Model):
    subject = models.ForeignKey(Subject, related_name='questions', on_delete=models.CASCADE)
    year = models.ForeignKey(Year, related_name='questions', on_delete=models.CASCADE, default=1)
    image = models.ImageField(blank=True, null=True)
    question = models.CharField(max_length=500)
    option_A = models.CharField(max_length=500)
    option_B = models.CharField(max_length=500)
    option_C = models.CharField(max_length=500)
    option_D = models.CharField(max_length=500)
    option_E = models.CharField(max_length=500, null=True, blank=True)
    ANSWER_CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
        ('E', 'Option E'),
    ]
    answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)

    class Meta:
        verbose_name = "WAEC Question"
        verbose_name_plural = "WAEC Questions"
        
    def __str__(self):
        return f"{self.question}"
    
    
    
