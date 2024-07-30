from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .service import call_ai_api

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
