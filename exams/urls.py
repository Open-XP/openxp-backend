from django.urls import path
from .views import (
    CreateQuestionAPIView,
    RetrieveQuestionAPIView,
    UpdateQuestionAPIView,
    DeleteQuestionAPIView,
    FilteredQuestionsAPIView,
    # ListAllQuestionsAPIView
)

urlpatterns = [
    path('questions/create/', CreateQuestionAPIView.as_view(), name='create-question'),
    path('questions/<int:pk>/', RetrieveQuestionAPIView.as_view(), name='retrieve-question'),
    path('questions/<int:pk>/update/', UpdateQuestionAPIView.as_view(), name='update-question'),
    path('questions/<int:pk>/delete/', DeleteQuestionAPIView.as_view(), name='delete-question'),
    path('questions/filter/', FilteredQuestionsAPIView.as_view(), name='filtered-questions'),
    # path('questions/all/', ListAllQuestionsAPIView.as_view(), name='list-all-questions'),
]
