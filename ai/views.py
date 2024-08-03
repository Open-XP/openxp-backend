from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .service import call_ai_api, call_ai_api2
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer
from rest_framework.permissions import IsAuthenticated

@method_decorator(csrf_exempt, name='dispatch')
class ExplainAnswersView(View):

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
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({"error": "Invalid request method"}, status=405)
    

class ChatSessionListCreateView(generics.ListCreateAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class ChatSessionDetailView(generics.RetrieveAPIView):
    queryset = ChatSession.objects.all()
    serializer_class = ChatSessionSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        user = request.user
        session_id = request.data.get('session_id', None)
        user_message = request.data.get('message', '')

        if not user_message:
            return Response({'error': 'Message content is required'}, status=status.HTTP_400_BAD_REQUEST)

        if session_id:
            try:
                session = ChatSession.objects.get(id=session_id, user=user)
            except ChatSession.DoesNotExist:
                return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            session = ChatSession.objects.create(user=user)

        user_message_instance = ChatMessage.objects.create(session=session, role='user', content=user_message)

        # Gather all messages from the session
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
