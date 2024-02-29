from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsUploader
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


class CreateQuestionAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsUploader]

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)


class RetrieveQuestionAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsUploader]


class UpdateQuestionAPIView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsUploader]


class DeleteQuestionAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsUploader]


class StandardResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class FilteredQuestionsAPIView(APIView):
    def get(self, request):
        queryset = Question.objects.all()

        # Retrieve query parameters
        year = request.query_params.get('year')
        exam_type_name = request.query_params.get('exam_type')
        subject_name = request.query_params.get('subject')
        topic_name = request.query_params.get('topic')

        # Apply filters if they exist
        if year:
            queryset = queryset.filter(uploaded_at__year=year)
        if exam_type_name:
            queryset = queryset.filter(exam_type__name__icontains=exam_type_name)
        if subject_name:
            queryset = queryset.filter(subject__name__icontains=subject_name)
        if topic_name:
            queryset = queryset.filter(topic__name__icontains=topic_name)

        # Pagination
        paginator = StandardResultsPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = QuestionSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
