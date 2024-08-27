# View.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from .service import call_ai_api, call_ai_api2
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer
import random
import string
from datetime import datetime
import re


class ExplainAnswersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt')
            if prompt:
                ai_response = call_ai_api(prompt)
                return JsonResponse(ai_response)
            else:
                return JsonResponse({"error": "No prompt provided"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)


class ChatSessionListCreateView(generics.ListCreateAPIView):
    serializer_class = ChatSessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return chat sessions belonging to the authenticated user
        return ChatSession.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user to the authenticated user
        serializer.save(user=self.request.user)

class ChatSessionDetailView(generics.RetrieveAPIView):
    serializer_class = ChatSessionSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return chat sessions belonging to the authenticated user
        return ChatSession.objects.filter(user=self.request.user)

class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, session_id, *args, **kwargs):
        user = request.user
        user_message = request.data.get('message', '')

        if not user_message:
            return Response({'error': 'Message content is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            session = ChatSession.objects.get(id=session_id, user=user)
        except ChatSession.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

        user_message_instance = ChatMessage.objects.create(session=session, role='user', content=user_message)

        all_messages = session.messages.all().order_by('timestamp')
        messages = [
            {"role": message.role, "content": message.content}
            for message in all_messages
        ]

        ai_response = call_ai_api2(messages)

        if "choices" in ai_response:
            response_content = ai_response['choices'][0]['message']['content']
            assistant_message_instance = ChatMessage.objects.create(session=session, role='assistant', content=response_content)
            response_serializer = ChatMessageSerializer(assistant_message_instance)
            return Response({'response': response_serializer.data}, status=status.HTTP_200_OK)
        else:
            error_message = ai_response.get('error', 'Unknown error')
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
class CareerSuggestionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        random_seed = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        prompt = (
            f"Please provide exactly three concise career-related questions for high school students "
            f"who are about to enter higher education. Each question should be a short header or question, "
            f"such as 'Can you', 'How do I', etc. The questions should be numbered 1, 2, and 3, and each on a new line. "
            f"Ensure each question is complete and clear. ({random_seed} - {timestamp})"
        )
        
        messages = [
            {"role": "system", "content": "You are an expert in career counseling for high school students transitioning to higher education."},
            {"role": "user", "content": prompt}
        ]

        ai_response = call_ai_api2(messages)

        if "choices" in ai_response:
            response_content = ai_response['choices'][0]['message']['content']

            # Use regular expressions to extract numbered questions
            questions = re.findall(r'\d+\.\s*(.*)', response_content)

            # Check for incomplete questions and retry if necessary
            if len(questions) < 3 or any(len(q.split()) < 5 for q in questions):
                error_message = "AI did not return enough complete topics"
                return JsonResponse({'error': error_message, 'topics_returned': questions}, status=500)

            # Ensure we return exactly 3 questions
            questions = questions[:3]
            return JsonResponse({'career_suggestions': questions}, status=200)
        else:
            error_message = ai_response.get('error', 'Unknown error')
            return JsonResponse({'error': error_message}, status=500)
        
        
class ChatSessionDeleteView(generics.DestroyAPIView):
    serializer_class = ChatSessionSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return chat sessions belonging to the authenticated user
        return ChatSession.objects.filter(user=self.request.user)