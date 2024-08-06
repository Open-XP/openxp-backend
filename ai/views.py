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
        prompt = f"Suggest four career-related questions that high school students who are about to get into higher education can ask about different career paths. Each question should be a short and concise question, such as 'Can you explain...', 'How do I...', etc. ({random_seed} - {timestamp})"
        
        messages = [
            {"role": "system", "content": "You are an expert in career counseling for high school students transitioning to higher education."},
            {"role": "user", "content": prompt}
        ]

        ai_response = call_ai_api2(messages)

        if "choices" in ai_response:
            response_content = ai_response['choices'][0]['message']['content']
            # Split the response by lines and filter out empty lines
            questions = [question.strip() for question in response_content.split('\n') if question.strip()]
            # Ensure we return exactly 4 questions
            if len(questions) >= 4:
                questions = questions[:4]
            else:
                error_message = "AI did not return enough questions"
                return JsonResponse({'error': error_message, 'questions_returned': questions}, status=500)
            return JsonResponse({'career_suggestions': questions}, status=200)
        else:
            error_message = ai_response.get('error', 'Unknown error')
            return JsonResponse({'error': error_message}, status=500)