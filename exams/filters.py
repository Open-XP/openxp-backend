# filters.py

import django_filters
from .waec_model import Questions

class QuestionsFilter(django_filters.FilterSet):
    class Meta:
        model = Questions
        fields = {
            'subject': ['exact'],
            'year': ['exact', 'gte', 'lte'],
            'question': ['icontains'],
        }
