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


def call_ai_api2(messages):
    api_url = 'https://api.ai71.ai/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.AI71_API_KEY}'
    }
    data = {
        "model": "tiiuae/falcon-180b-chat",
        "messages": messages
    }
    try:
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return {"error": "Failed to get response from AI service"}