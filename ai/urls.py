from django.urls import path
from .views import ExplainAnswersView, ChatSessionListCreateView, ChatSessionDetailView, ChatView

urlpatterns = [
    path('explain_answers/', ExplainAnswersView.as_view(), name='explain_answers'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('sessions/', ChatSessionListCreateView.as_view(), name='list_chat_sessions'),
    path('sessions/<int:id>/', ChatSessionDetailView.as_view(), name='chat_session_detail'),
]