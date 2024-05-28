from rest_framework import generics
from .waec_model import Questions 
from .serializers import WAECQuestionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsUploader
from django_filters.rest_framework import DjangoFilterBackend
from .filters import QuestionsFilter
from rest_framework.pagination import PageNumberPagination

class CreateWAECQuestionAPIView(generics.CreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = WAECQuestionSerializer
    permission_classes = [IsUploader]
    

class StandardResultsPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'  # Allow client to specify the page size
    max_page_size = 20 


class ListWAECQuestionAPIView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = WAECQuestionSerializer
    permission_classes = [IsUploader]
    filter_backends = [DjangoFilterBackend]
    filterset_class = QuestionsFilter
    pagination_class = StandardResultsPagination


class RetrieveWAECQuestionAPIView(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = WAECQuestionSerializer
    permission_classes = [IsUploader]


class UpdateWAECQuestionAPIView(generics.UpdateAPIView):
    queryset = Questions.objects.all()
    serializer_class = WAECQuestionSerializer
    permission_classes = [IsUploader]


class DeleteWAECQuestionAPIView(generics.DestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = WAECQuestionSerializer
    permission_classes = [IsUploader]
