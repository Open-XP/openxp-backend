# from rest_framework import serializers
# from .models import Question

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = '__all__'  


from rest_framework import serializers
from .waec_model import WAEC, Questions


class WAECQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"
