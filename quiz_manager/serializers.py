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

waec_instance = WAEC()

class TestInstanceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    exam = serializers.SlugRelatedField(slug_field='id', queryset=WAEC.objects.all())
    subject = serializers.SlugRelatedField(slug_field='name', queryset=Subject.objects.all())
    year = serializers.SlugRelatedField(slug_field='year', queryset=Year.objects.all())
    
    class Meta:
        model = TestInstance
        fields = [
            'id', 
            'duration',
            'user', 
            'exam', 
            'subject', 
            'year', 
            'start_time', 
            'end_time', 
            'is_completed',
            ]
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
    total_time = FormattedDurationField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserScore
        fields = [
            'id',
            'user',
            'total_questions',
            'total_time',
            'score',
            'date',
            'test_instance',
            'correct_questions',
            'incorrect_questions',
        ]

    def get_user(self, obj):
        return obj.test_instance.user.id  
        

class TotalStudyTimeSerializer(serializers.ModelSerializer):
    overall_study_time = FormattedDurationField()

    class Meta:
        model = TotalStudyTime
        fields = ( 'overall_study_time',)
        
        
class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['year']

class SubjectSerializer(serializers.ModelSerializer):
    years = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ['name', 'exam', 'years']

    def get_years(self, obj):
        # Get unique years associated with the subject's questions.
        years = Year.objects.filter(questions__subject=obj).distinct()
        return YearSerializer(years, many=True).data
    
    

