from django.urls import path
from .views import ExplainAnswersView

urlpatterns = [
    path('explain_answers/', ExplainAnswersView.as_view(), name='explain_answers'),
]