from rest_framework import serializers
from .models import ChatSession, ChatMessage, GenerateLearningContentContainer, Subject, Topic, Question, TestInstance, UserAnswer  

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'

class ChatSessionSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = '__all__'
        read_only_fields = ['user',]
        
        
class GenerateLearningContentContainerSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(
    queryset=Subject.objects.all(),
    slug_field='name' 
    )
    
    topic = serializers.SlugRelatedField(
    queryset=Topic.objects.all(),
    slug_field='name'
    )
    
    class Meta:
        model = GenerateLearningContentContainer
        fields = '__all__'
        read_only_fields = ['user', 'created_at']
        

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        

class TestInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestInstance
        fields = '__all__'
        read_only_fields = ['user', 'score', 'completed_at']
        
        
class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'
        read_only_fields = ['is_correct']