from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from .models import TestInstance, Questions, WAEC, Subject, Year, UserAnswer, UserScore
from .serializers import TestInstanceSerializer, QuestionSerializer, UserAnswerSerializer, UserScoreSerializer


class StartTestAPIView(generics.CreateAPIView):
    serializer_class = TestInstanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        exam_id = self.request.data.get('exam')
        subject_id = self.request.data.get('subject')
        year_id = self.request.data.get('year')

        exam = get_object_or_404(WAEC, id=exam_id)
        subject = get_object_or_404(Subject, id=subject_id, exam=exam)
        year = get_object_or_404(Year, id=year_id)

        questions = Questions.objects.filter(subject=subject, year=year)[:exam.total_questions]
        if questions.count() < exam.total_questions:
            return Response({'error': 'Not enough questions available for the given subject and year.'}, status=status.HTTP_400_BAD_REQUEST)

        test_instance = serializer.save(user=user, exam=exam, subject=subject, year=year)
        test_instance.questions.set(questions)
        test_instance.save()


        return Response(TestInstanceSerializer(test_instance).data, status=status.HTTP_201_CREATED)


class RetrieveAllTestInstancesAPIView(generics.ListAPIView):
    serializer_class = TestInstanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TestInstance.objects.filter(user=user)
    


class DeleteTestInstanceAPIView(generics.DestroyAPIView):
    serializer_class = TestInstanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TestInstance.objects.filter(user=self.request.user)


class RetrieveQuestionsAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        test_instance_id = self.kwargs['test_instance_id']
        test_instance = get_object_or_404(TestInstance, id=test_instance_id, user=self.request.user)
        return test_instance.questions.all()
    

class RetrieveIndividualQuestionsAPIView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        test_instance_id = self.kwargs['test_instance_id']
        question_id = self.kwargs['question_id']
        test_instance = get_object_or_404(TestInstance, id=test_instance_id, user=self.request.user)
        question = get_object_or_404(test_instance.questions.all(), id=question_id)
        return question


class SubmitAnswerAPIView(generics.CreateAPIView):
    serializer_class = UserAnswerSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        test_instance_id = request.data.get('test_instance')
        question_id = request.data.get('question')
        selected_option = request.data.get('selected_option')

        # Retrieve the test instance and question objects
        test_instance = get_object_or_404(TestInstance, id=test_instance_id, user=request.user)
        question = get_object_or_404(test_instance.questions.all(), id=question_id)

        # Check if an answer already exists
        user_answer, created = UserAnswer.objects.get_or_create(
            test_instance=test_instance,
            question=question,
            defaults={'selected_option': selected_option}
        )

        # If the answer was not just created, update the selected_option
        if not created:
            user_answer.selected_option = selected_option
            user_answer.is_correct = question.answer == selected_option  # Re-check correctness in case the answer was updated
            user_answer.save()

        return Response(UserAnswerSerializer(user_answer).data)


class CompleteTestAPIView(generics.UpdateAPIView):
    queryset = TestInstance.objects.all()
    serializer_class = TestInstanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        test_instance = self.get_object()
        if test_instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to modify this test instance.")
        if test_instance.is_completed:
            return Response({'message': 'Test is already completed'}, status=400)

        # Using the correct related_name 'answers'
        answers = test_instance.answers.all()
        correct_answers = answers.filter(is_correct=True)
        incorrect_answers = answers.filter(is_correct=False)

        # Calculate score and update UserScore
        score = (correct_answers.count() / answers.count()) * 100 if answers.count() > 0 else 0
        user_score, created = UserScore.objects.get_or_create(
            test_instance=test_instance,
            defaults={'score': score}
        )
        user_score.correct_questions.set(correct_answers.values_list('question', flat=True))
        user_score.incorrect_questions.set(incorrect_answers.values_list('question', flat=True))
        user_score.save()

        serializer.save(end_time=timezone.now(), is_completed=True)

        return Response({'message': 'Test completed successfully'}, status=status.HTTP_200_OK)


class UserScoreAPIView(generics.RetrieveAPIView):
    serializer_class = UserScoreSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        test_instance_id = self.kwargs['test_instance_id']
        test_instance = get_object_or_404(TestInstance, id=test_instance_id, user=self.request.user)
        user_score = get_object_or_404(UserScore, test_instance=test_instance)
        return user_score


class CompletedTestsAPIView(generics.ListAPIView):
    serializer_class = TestInstanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TestInstance.objects.filter(is_completed=True, user=self.request.user)


class TestResultAPIView(generics.RetrieveAPIView):
    serializer_class = TestInstanceSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        test_instance_id = self.kwargs['test_instance_id']
        test_instance = get_object_or_404(TestInstance, id=test_instance_id, user=self.request.user)
        answers = UserAnswer.objects.filter(test_instance=test_instance)
        correct_answers = answers.filter(is_correct=True).count()
        total_questions = answers.count()

        result = {
            "correct_answers": correct_answers,
            "total_questions": total_questions,
            "score": correct_answers / total_questions * 100 if total_questions > 0 else 0
        }

        return Response(result)
