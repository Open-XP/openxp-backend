# from django.db import models
# from django.conf import settings
# from django.utils import timezone

# class Exam(models.Model):
#     exam_type = models.CharField(max_length=100, unique=True)
#     title = models.CharField(max_length=200)
#     description = models.TextField()

#     class Meta:
#         verbose_name = 'Exam'
#         verbose_name_plural = 'Exams'

#     def __str__(self):
#         return self.title

# class Subject(models.Model):
#     name = models.CharField(max_length=40)
#     exam = models.ForeignKey(Exam, related_name='subjects', on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = 'Subject'
#         verbose_name_plural = 'Subjects'
#         unique_together = ('name', 'exam')

#     def __str__(self):
#         return f"{self.name} ({self.exam})"

# class Grade(models.Model):
#     OPTION_CHOICES = [
#         ('SS1', 'SS 1'),
#         ('SS2', 'SS 2'),
#         ('SS3', 'SS 3'),
#     ]

#     name = models.CharField(max_length=15, choices=OPTION_CHOICES)

#     class Meta:
#         verbose_name = 'Grade'
#         verbose_name_plural = 'Grades'

#     def __str__(self):
#         return self.get_name_display()  # This will return the human-readable name for the choice

# class Topic(models.Model):
#     subject = models.ForeignKey(Subject, related_name='topics', on_delete=models.CASCADE)
#     grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='topics', default=None)
#     name = models.CharField(max_length=40)

#     class Meta:
#         verbose_name = 'Topic'
#         verbose_name_plural = 'Topics'
#         unique_together = ('name', 'grade', 'subject')

#     def __str__(self):
#         return self.name

# class Question(models.Model):
#     OPTION_CHOICES = [
#         ('A', 'Option A'),
#         ('B', 'Option B'),
#         ('C', 'Option C'),
#         ('D', 'Option D'),
#         ('E', 'Option E'),
#     ]

#     topic = models.ForeignKey(
#         Topic,
#         related_name='questions', 
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         default=None                 
#     )
    
#     subject = models.ForeignKey(
#         Subject, 
#         on_delete=models.SET_NULL, 
#         null=True, 
#         blank=True, 
#         default=None
#     )

#     text = models.TextField()
#     mark = models.PositiveIntegerField()
#     image = models.ImageField(upload_to='questions/', blank=True, null=True)
#     correct_answer = models.CharField(max_length=1, choices=OPTION_CHOICES)
#     option_a = models.CharField(max_length=255)
#     option_b = models.CharField(max_length=255)
#     option_c = models.CharField(max_length=255)
#     option_d = models.CharField(max_length=255)
#     option_e = models.CharField(max_length=255)

#     uploader = models.ForeignKey(
#         settings.AUTH_USER_MODEL, 
#         related_name='uploaded_questions', 
#         on_delete=models.SET_NULL, 
#         null=True, 
#         blank=True
#     )

#     uploaded_at = models.DateTimeField(default=timezone.now)
    
#     class Meta:
#         verbose_name = 'Question'
#         verbose_name_plural = 'Questions'

#     def __str__(self):
#         return self.text

#     def save(self, *args, **kwargs):
#         if self.pk:  # Checking if the object already exists in the database
#             original = Question.objects.get(pk=self.pk)
#             if original.uploader is not None:
#                 self.uploader = original.uploader  # Preventing change of uploader
#         super(Question, self).save(*args, **kwargs)

# # Default methods (placed after the model definitions)
# def get_default_grade():
#     grade, created = Grade.objects.get_or_create(name="nullgrade")
#     return grade.id

# def get_default_subject():
#     subject, created = Subject.objects.get_or_create(name="nullsubject", exam_id=1)
#     return subject.id

# def get_default_topic():
#     topic, created = Topic.objects.get_or_create(name="nulltopic", subject_id=1, grade_id=1)
#     return topic.id
