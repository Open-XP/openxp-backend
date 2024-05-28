from rest_framework import serializers
from .fields import FormattedDurationField
from .models import (
                    TestInstance, 
                    UserAnswer, 
                    Questions, 
                    UserScore, 
                    WAEC, 
                    Subject,
                    Year,
                    TotalStudyTime,
                    )


class TestInstanceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    exam = serializers.SlugRelatedField(slug_field='id', queryset=WAEC.objects.all())
    subject = serializers.SlugRelatedField(slug_field='name', queryset=Subject.objects.all())
    year = serializers.SlugRelatedField(slug_field='year', queryset=Year.objects.all())

    class Meta:
        model = TestInstance
        fields = ['id', 
                  'user', 
                  'exam', 
                  'subject', 
                  'year', 
                  'start_time', 
                  'end_time', 
                  'is_completed']
        read_only_fields = ['user',]


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
        fields = ['id',
                  'total_time',
                  'score',
                  'test_instance',
                  'correct_questions',
                  'incorrect_questions',
                  'total_time',]
        

class TotalStudyTimeSerializer(serializers.ModelSerializer):
    overall_study_time = FormattedDurationField()

    class Meta:
        model = TotalStudyTime
        fields = ('user', 'overall_study_time')
