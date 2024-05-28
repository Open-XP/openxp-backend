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
)

urlpatterns = [
    path('exams/start-test/', StartTestAPIView.as_view(), name='start-test'),
    path('exams/all-test-instances/', RetrieveAllTestInstancesAPIView.as_view(), name='all-test-instances'),
    path('exams/test-instances/<int:test_instance_id>/questions/<int:question_id>/', RetrieveIndividualQuestionsAPIView.as_view(), name='retrieve-individual-question'),
    path('exams/<int:pk>/delete/', DeleteTestInstanceAPIView.as_view(), name='delete-test-instance'),
    path('exams/questions/<int:test_instance_id>/', RetrieveQuestionsAPIView.as_view(), name='retrieve-questions'),
    path('exams/submit-answer/', SubmitAnswerAPIView.as_view(), name='submit-answer'),
    path('exams/complete-test/<int:pk>/', CompleteTestAPIView.as_view(), name='complete-test'),
    path('exams/<int:test_instance_id>/results/', TestResultAPIView.as_view(), name='test-results'),
    path('exams/user-score/<int:test_instance_id>/', UserScoreAPIView.as_view(), name='user-score'),
    path('exams/completed-tests/', CompletedTestsAPIView.as_view(), name='completed-tests'),
    path('exams/total-study-time/', TotalStudyTimeAPIView.as_view(), name='total-study-time'),
]
