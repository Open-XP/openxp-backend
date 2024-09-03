from django.urls import path
from .views import (
    ExplainAnswersView,
    ChatSessionListCreateView,
    ChatSessionDetailView,
    ChatView,
    CareerSuggestionsView,
    ChatSessionDeleteView,
    GenerateSpecificContentView,
    GenerateLearningContentContainerView,
    GenerateDetailedNoteView,
    GenerateQuestionsAndCreateTestView,
    ListQuestionsView,
    TestInstanceQuestionsView, 
    )

urlpatterns = [
    path('explain_answers/', ExplainAnswersView.as_view(), name='explain_answers'),
    path('chat/<int:session_id>/', ChatView.as_view(), name='chat'),
    path('sessions/', ChatSessionListCreateView.as_view(), name='list_chat_sessions'),
    path('sessions/<int:id>/', ChatSessionDetailView.as_view(), name='chat_session_detail'),
    path('sessions/delete/<int:id>/', ChatSessionDeleteView.as_view(), name='delete_chat_session'),
    path('career-suggestions/', CareerSuggestionsView.as_view(), name='career-suggestions'),
    path('generate-learning-content/', GenerateLearningContentContainerView.as_view(), name='generate_learning_content_container'),
    path('generate-specific-content/', GenerateSpecificContentView.as_view(), name='generate_specific_content'),
    path('generate-detailed-note/', GenerateDetailedNoteView.as_view(), name='generate_detailed_note'),
    path('generate-questions-create-test/', GenerateQuestionsAndCreateTestView.as_view(), name='generate_questions_create_test'),
    path('generated-questions/', ListQuestionsView.as_view(), name='list_questions'),
    path('generated-test-instance/<str:test_instance_id>/', TestInstanceQuestionsView.as_view(), name='test-instance-questions'),
]