from rest_framework import serializers
from .models import TestInstance, UserAnswer, Questions, UserScore


class TestInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestInstance
        fields = ['id', 'user', 'exam', 'subject', 'year', 'start_time', 'end_time', 'is_completed']
        read_only_fields = ['start_time', 'end_time', 'is_completed']


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
        # exclude = ['answer',]
        # fields =  ['id', 'image', 'question', 'option_A', 'option_B', 'option_C', 'option_D', 'option_E',  'subject', 'year']
        
    

class UserScoreSerializer(serializers.ModelSerializer):
    correct_questions = QuestionSerializer(many=True, read_only=True)
    incorrect_questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = UserScore
        fields = ['id', 'score', 'test_instance', 'correct_questions', 'incorrect_questions']
