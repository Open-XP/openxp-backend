from django.urls import path
from .views import (
    StartTestAPIView,
    RetrieveQuestionsAPIView,
    SubmitAnswerAPIView,
    CompleteTestAPIView,
    TestResultAPIView,
    CompletedTestsAPIView,
    RetrieveAllTestInstancesAPIView,
    DeleteTestInstanceAPIView,
    RetrieveIndividualQuestionsAPIView,
    UserScoreAPIView,
    TotalStudyTimeAPIView,
    SubjectListAPIView,
)

urlpatterns = [
    path('exams/start-test/', StartTestAPIView.as_view(), name='start-test'),
    path('exams/all-test-instances/', RetrieveAllTestInstancesAPIView.as_view(), name='all-test-instances'),
    path('exams/test-instances/<str:test_instance_id>/questions/<str:question_id>/', RetrieveIndividualQuestionsAPIView.as_view(), name='retrieve-individual-question'),
    path('exams/<str:pk>/delete/', DeleteTestInstanceAPIView.as_view(), name='delete-test-instance'),
    path('exams/questions/<str:test_instance_id>/', RetrieveQuestionsAPIView.as_view(), name='retrieve-questions'),
    path('exams/submit-answer/', SubmitAnswerAPIView.as_view(), name='submit-answer'),
    path('exams/complete-test/<str:pk>/', CompleteTestAPIView.as_view(), name='complete-test'),
    path('exams/<str:test_instance_id>/results/', TestResultAPIView.as_view(), name='test-results'),
    path('exams/user-score/<str:test_instance_id>/', UserScoreAPIView.as_view(), name='user-score'),
    path('exams/completed-tests/', CompletedTestsAPIView.as_view(), name='completed-tests'),
    path('exams/total-study-time/', TotalStudyTimeAPIView.as_view(), name='total-study-time'),
    path('subjects/', SubjectListAPIView.as_view(), name='subject-list'),
]
