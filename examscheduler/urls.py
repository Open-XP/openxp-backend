from django.urls import path
from .views import ExamListCreateView, ExamRetrieveUpdateDestroyView

urlpatterns = [
    path('exams/', ExamListCreateView.as_view(), name='exam-list-create'),
    path('exams/<int:pk>/', ExamRetrieveUpdateDestroyView.as_view(), name='exam-detail'),
]