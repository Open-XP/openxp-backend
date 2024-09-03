from django.db import models
from django.conf import settings
import uuid

class ChatSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_sessions')
    started_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatSession {self.id} for user {self.user.username}"

class ChatMessage(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=10) 
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role.capitalize()} message in session {self.session.id}"

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class GenerateLearningContentContainer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='learning_content_containers')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='learning_content_containers')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='learning_content_containers')
    grade = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=2)
    introduction = models.TextField(null=True, blank=True)
    learning_objectives = models.JSONField(default=dict, blank=True)
    dynamic_content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Learning Content for {self.subject.name} - {self.topic.name} ({self.grade} grade)"
    
    
class Question(models.Model):
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
        ]
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question: {self.question_text} - Correct Answer: {self.correct_answer}"
    
    
class TestInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ai_test_instances')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Test Instance for {self.user.username} on {self.topic.name} - Score: {self.score if self.score else 'Not completed'}"
    
    
class UserAnswer(models.Model):
    test_instance = models.ForeignKey(TestInstance, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1, choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')])
    is_correct = models.BooleanField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.is_correct = self.selected_option == self.question.correct_answer
        super(UserAnswer, self).save(*args, **kwargs)

    def __str__(self):
        return f"Answer to {self.question.question_text} by {self.test_instance.user.username}: {'Correct' if self.is_correct else 'Incorrect'}"