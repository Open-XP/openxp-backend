from rest_framework import serializers
from .models import ExamScheduler 

class ExamSchedulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamScheduler
        fields = '__all__'
        read_only_fields = ['user',]