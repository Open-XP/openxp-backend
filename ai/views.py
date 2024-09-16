# View.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from .service import call_ai_api, call_ai_api2
from django.shortcuts import get_object_or_404
from .models import (
                    ChatSession,
                    ChatMessage, 
                    GenerateLearningContentContainer, 
                    Subject,
                    Topic, 
                    Question, 
                    TestInstance,
                    UserAnswer,
                    )
from .serializers import (
                        ChatSessionSerializer, 
                        ChatMessageSerializer, 
                        GenerateLearningContentContainerSerializer, 
                        QuestionSerializer, 
                        TestInstanceSerializer, 
                        UserAnswerSerializer,
                        SubjectSerializer,
                        TopicSerializer,
                        )
from rest_framework.response import Response
import random
import string
from datetime import datetime
from django.utils import timezone
import re
import json


class ExplainAnswersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt')
            print('Prompt:', prompt)
            if prompt:
                ai_response = call_ai_api(prompt)
                return JsonResponse(ai_response, safe=False)
            else:
                return JsonResponse({"error": "No prompt provided"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)


class ChatSessionListCreateView(generics.ListCreateAPIView):
    serializer_class = ChatSessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ChatSession.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChatSessionDetailView(generics.RetrieveAPIView):
    serializer_class = ChatSessionSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
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

            questions = re.findall(r'\d+\.\s*(.*)', response_content)

            if len(questions) < 3 or any(len(q.split()) < 5 for q in questions):
                error_message = "AI did not return enough complete topics"
                return JsonResponse({'error': error_message, 'topics_returned': questions}, status=500)

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
        return ChatSession.objects.filter(user=self.request.user)
    

class GenerateQuestionsAndCreateTestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Extract input data from the request
        subject_name = request.data.get('subject')
        topic_name = request.data.get('topic')

        # Validate subject and topic input
        if not subject_name or not topic_name:
            return Response({"error": "Subject and topic are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Get additional parameters, with defaults
        num_questions = request.data.get('num_questions', 5)
        difficulty = request.data.get('difficulty', 1)

        try:
            # Fetch subject and topic from the database
            subject = get_object_or_404(Subject, name=subject_name)
            topic = get_object_or_404(Topic, name=topic_name)

            # Form the prompt for AI generation
            prompt = (
                f"Generate '{num_questions}' unique questions of '{difficulty}/10' "
                f"for the topic '{topic.name}' under the subject '{subject.name}' "
                f"with options A, B, C, D, and answer for each question. "
                f"Just generate questions, do not add any comment that are not part of the question. "
                f"The questions and answers should be in JSON format with keys 'question', 'options' and 'answer'."
            )

            # Call the AI API to generate questions
            generated_questions = call_ai_api(prompt)
            print("Raw AI Response:", generated_questions)

            # Ensure the AI response contains choices and parse it
            if "choices" in generated_questions and len(generated_questions['choices']) > 0:
                generated_questions = generated_questions['choices'][0]['message']['content']
                questions_list = self.clean_and_parse_json(generated_questions)
                print("Parsed Questions:", questions_list)
            else:
                return Response({"error": "AI failed to generate valid questions."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # If the questions list is empty, return an error
            if not questions_list:
                return Response({"error": "Failed to generate valid questions."}, status=status.HTTP_400_BAD_REQUEST)

            # Process and save each question
            questions = []
            for generated_question in questions_list:
                question_data = {
                    "question_text": generated_question['question'],
                    "option_a": generated_question['options']['A'],
                    "option_b": generated_question['options']['B'],
                    "option_c": generated_question['options']['C'],
                    "option_d": generated_question['options']['D'],
                    "correct_answer": generated_question['answer'],
                    "subject": subject.id,
                    "topic": topic.id,
                }

                # Serialize and validate the question
                serializer = QuestionSerializer(data=question_data)
                if serializer.is_valid():
                    question = serializer.save()
                    questions.append(question)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # Create the test instance if questions were successfully generated
            test_instance = TestInstance.objects.create(user=request.user, subject=subject, topic=topic)
            test_instance.questions.set(questions)
            test_instance.save()

            # Return the created test instance and success message
            return Response({
                "test_instance": TestInstanceSerializer(test_instance).data,
                "message": f"{len(questions)} questions generated and test instance created successfully."
            }, status=status.HTTP_201_CREATED)

        except Subject.DoesNotExist:
            return Response({"error": "Subject not found."}, status=status.HTTP_404_NOT_FOUND)
        except Topic.DoesNotExist:
            return Response({"error": "Topic not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def clean_and_parse_json(self, json_string):
        """
        Cleans and parses AI-generated JSON from a string.
        """
        try:
            # Clean the string: remove any unnecessary escape sequences, markdown, or newlines
            cleaned_string = json_string.replace('\\n', '').replace('\\', '').strip()

            # Strip out JSON delimiters if present (e.g., ```json or ``` wrapping)
            cleaned_string = re.sub(r'```json|```', '', cleaned_string)

            # Validate and parse the JSON string
            questions_data = json.loads(cleaned_string)
            
            # Ensure the parsed data is a list of dictionaries
            if not isinstance(questions_data, list):
                raise ValueError("Parsed JSON is not a list of questions")

            # Ensure every question contains 'question', 'options', and 'answer'
            for question in questions_data:
                if not all(key in question for key in ['question', 'options', 'answer']):
                    raise ValueError(f"Invalid question format: {question}")
                if not all(opt in question['options'] for opt in ['A', 'B', 'C', 'D']):
                    raise ValueError(f"Options missing for question: {question}")

            return questions_data

        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error decoding or validating JSON: {e}")
            return []
    

class TestInstanceQuestionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, test_instance_id, *args, **kwargs):
        test_instance = get_object_or_404(TestInstance, id=test_instance_id, user=request.user)
        questions = test_instance.questions.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

            
class GenerateLearningContentContainerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = GenerateLearningContentContainerSerializer(data=request.data)
        if serializer.is_valid():
            container = serializer.save(user=request.user)
            return Response(GenerateLearningContentContainerSerializer(container).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RetrieveLearningContentContainerView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, learning_content_container_id, *args, **kwargs):
        container = get_object_or_404(GenerateLearningContentContainer, id=learning_content_container_id, user=request.user)
        return Response(GenerateLearningContentContainerSerializer(container).data, status=status.HTTP_200_OK)
    

class SubmitAnswerView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserAnswerSerializer
    
    def post(self, request, *args, **kwargs):
        test_instance_id = request.data.get('test_instance')
        question_id = request.data.get('question')
        selected_option = request.data.get('selected_option')
        
        test_instance = get_object_or_404(TestInstance, id=test_instance_id, user=request.user)
        question = get_object_or_404(Question, id=question_id)
        
        user_answer, created = UserAnswer.objects.get_or_create(
            test_instance=test_instance,
            question=question,
            defaults={'selected_option': selected_option}
        )
        
        if not created:
            user_answer.selected_option = selected_option
            user_answer.is_correct = question.correct_answer == selected_option
            user_answer.save()
            
        return Response(UserAnswerSerializer(user_answer).data, status=status.HTTP_200_OK)
    

class CompleteGeneratedLearningContentView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GenerateLearningContentContainerSerializer
    
    def post(self, request, *args, **kwargs):
        learning_content_container_id = request.data.get('learning_content_container_id')
        
        if not learning_content_container_id:
            return Response({"error": "learning_content_container_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        container = get_object_or_404(GenerateLearningContentContainer, id=learning_content_container_id, user=request.user)
        container.is_completed = True
        container.save()
        
        return Response(GenerateLearningContentContainerSerializer(container).data, status=status.HTTP_200_OK)
        
        
class ListSubjectsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    

class DeleteLearningContentContainerView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, learning_content_container_id, *args, **kwargs):
        container = get_object_or_404(GenerateLearningContentContainer, id=learning_content_container_id, user=request.user)
        container.delete()
        return Response({"message": "Learning content container deleted successfully."}, status=status.HTTP_200_OK)
       

class GenerateSpecificContentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        container_id = request.data.get('id')
        section_type = request.data.get('section_type')

        if not section_type:
            return Response({"error": "The 'section_type' field is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            container = GenerateLearningContentContainer.objects.get(id=container_id, user=request.user)
            
            if container.is_completed:
                return Response({"error": "Lesson is already completed"}, status=status.HTTP_400_BAD_REQUEST)


            prompt = self.generate_prompt(container.subject, container.topic, container.grade, section_type)
            generated_content = call_ai_api(prompt)

            if "choices" in generated_content:
                generated_content = generated_content['choices'][0]['message']['content']

            if section_type == 'introduction':
                container.introduction = generated_content
            elif section_type == 'learning_objectives':
                self.store_learning_objectives(container, generated_content)
            else:
                container.dynamic_content[section_type] = generated_content

            container.save()

            return Response(GenerateLearningContentContainerSerializer(container).data, status=status.HTTP_200_OK)

        except GenerateLearningContentContainer.DoesNotExist:
            return Response({"error": "Learning content container not found."}, status=status.HTTP_404_NOT_FOUND)

    def store_learning_objectives(self, container, learning_objectives):
        objectives = re.split(r'\n\d+\.\s*', learning_objectives)
        objectives = [obj.strip() for obj in objectives if obj.strip()]
        container.learning_objectives = {f'learning_objective_{i}': objective for i, objective in enumerate(objectives, start=1)}

    def generate_prompt(self, subject, topic, grade, section_type):
        if section_type == 'introduction':
            return f"I dont want any comment like certainly, Just start with what you are asked to do which is to provide a brief introduction to the topic '{topic.name}' under the subject '{subject.name}', suitable for a {grade}th-grade student."
        elif section_type == 'learning_objectives':
            return f"Do not say anything that is not a learning content just generate List 10 key learning objectives for the topic '{topic.name}' under the subject '{subject.name}', targeting a {grade}th-grade student."

        
class GenerateDetailedNoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        container_id = request.data.get('id')
        learning_objective_key = request.data.get('learning_objective_key')

        try:
            container = GenerateLearningContentContainer.objects.get(id=container_id, user=request.user)

            if learning_objective_key not in container.learning_objectives:
                return Response({"error": f"Learning objective '{learning_objective_key}' not found."}, status=status.HTTP_404_NOT_FOUND)

            objective = container.learning_objectives[learning_objective_key]
            prompt = (
                f"Provide detailed notes for the following learning objective with difficulty '{container.difficulty}/10' note **Warning no extra non related texts just go straight to generating learning objectives: '{objective}' "
                f"under the subject '{container.subject.name}' in a detailed but easy-to-understand manner for a {container.grade}th-grade student."
            )
            print('Generate detailed note prompt:', prompt)
            detailed_note = call_ai_api(prompt)
            if "choices" in detailed_note:
                detailed_note = detailed_note['choices'][0]['message']['content']

            detailed_note_key = f'detailed_{learning_objective_key}'
            container.dynamic_content[detailed_note_key] = detailed_note
            container.save()

            total_objectives = len(container.learning_objectives)
            generated_objectives = len([key for key in container.dynamic_content.keys() if key.startswith('detailed_learning_objective_')])
 
            response_data = {
                "detailed_learning_body": {key: value for key, value in container.dynamic_content.items() if key.startswith('detailed_')},
                "total_number_of_learning_objectives": total_objectives,
                "learning_objectives_generated": generated_objectives
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except GenerateLearningContentContainer.DoesNotExist:
            return Response({"error": "Learning content container not found."}, status=status.HTTP_404_NOT_FOUND)
        

class ListQuestionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        subject_id = request.query_params.get('subject')
        topic_id = request.query_params.get('topic')

        questions = Question.objects.all()

        if subject_id:
            questions = questions.filter(subject_id=subject_id)

        if topic_id:
            questions = questions.filter(topic_id=topic_id)

        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)
    
class CompleteTestAndScoreView(APIView):
    def post(self, request, *args, **kwargs):
        test_instance_id = request.data.get('test_instance_id')

        try:
            test_instance = TestInstance.objects.get(id=test_instance_id, user=request.user)
        except TestInstance.DoesNotExist:
            return Response({"error": "Test instance not found."}, status=status.HTTP_404_NOT_FOUND)

        if test_instance.is_completed:
            return Response({"error": "Test is already completed."}, status=status.HTTP_400_BAD_REQUEST)

        user_answers = UserAnswer.objects.filter(test_instance=test_instance)

        correct_questions = []
        incorrect_questions = []
        total_questions = test_instance.questions.count()

        correct_answers_count = 0
        for answer in user_answers:
            if answer.is_correct:
                correct_questions.append(answer.question.id)
                correct_answers_count += 1
            else:
                incorrect_questions.append(answer.question.id)

        score = (correct_answers_count / total_questions) * 100 if total_questions > 0 else 0

        test_instance.is_completed = True
        test_instance.score = score
        test_instance.completed_at = timezone.now()
        test_instance.save()

        return Response({
            "message": "simulated test completed"
        }, status=status.HTTP_200_OK)    
        
        
class FetchTestResultsView(generics.RetrieveAPIView):
    serializer_class = TestInstanceSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        test_instance_id = self.kwargs['test_instance_id']
        test_instance = get_object_or_404(TestInstance, id=test_instance_id, user=self.request.user, is_completed=True)
        return test_instance

    def get(self, request, *args, **kwargs):
        test_instance = self.get_object()

        user_answers = test_instance.user_answers.all()
        
        correct_answers = user_answers.filter(is_correct=True)
        incorrect_answers = user_answers.filter(is_correct=False)

        correct_questions = QuestionSerializer([answer.question for answer in correct_answers], many=True).data
        incorrect_questions = QuestionSerializer([answer.question for answer in incorrect_answers], many=True).data

        return Response({
            "test_instance_id": str(test_instance.id),
            "score": test_instance.score,
            "correct_questions": correct_questions,
            "incorrect_questions": incorrect_questions,
            "completed_at": test_instance.completed_at
        }, status=status.HTTP_200_OK)

    
class ExplainInAnEasyToUnderstandManner(APIView):
    permission_classes = [IsAuthenticated]
    pass
       