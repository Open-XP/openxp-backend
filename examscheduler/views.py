# schedule/views.py
from rest_framework import generics
from .models import ExamScheduler
from .serializers import ExamSchedulerSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class ExamListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamSchedulerSerializer

    def get_queryset(self):
        
        return ExamScheduler.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamSchedulerSerializer

    def get_queryset(self):
        return ExamScheduler.objects.filter(user=self.request.user)
