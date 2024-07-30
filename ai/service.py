# services/ai_service.py
import requests
from django.conf import settings

def call_ai_api(prompt):
    api_url = 'https://api.ai71.ai/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.AI71_API_KEY}'  # Use f-string for interpolation
    }
    # Print the authorization header to the console for debugging
    print(f"Authorization header: {headers['Authorization']}")
    
    data = {
        "model": "tiiuae/falcon-180b-chat",
        "messages": [
            {
                "role": "system",
                "content": "You are a highschool teacher."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    response = requests.post(api_url, json=data, headers=headers)
    return response.json()
