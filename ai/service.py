import requests
from django.conf import settings

def call_ai_api(prompt):
    api_url = 'https://api.ai71.ai/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.AI71_API_KEY}'  # Use f-string for interpolation
    }
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
        ],
        "max_tokens": 100,  # Adjust as needed
        "temperature": 0.7,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.5,
        "top_p": 0.9,
        "top_k": 50,
        "n": 1,
        "stop": ["career", "topic", "question", "education"]  # Adding word-based stop tokens
    }
    try:
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return {"error": "Request error: Unable to connect to AI service"}
    except Exception as err:
        print(f"Unexpected error occurred: {err}")
        return {"error": "Unexpected error: Unable to connect to AI service"}

def call_ai_api2(messages):
    api_url = 'https://api.ai71.ai/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.AI71_API_KEY}'
    }
    data = {
        "model": "tiiuae/falcon-180b-chat",
        "messages": messages,
        "max_tokens": 100,  # Adjust as needed
        "temperature": 0.7,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.5,
        "top_p": 0.9,
        "top_k": 50,
        "n": 1,
        "stop": ["career", "topic", "question", "education"]  # Adding word-based stop tokens
    }
    try:
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return {"error": "Request error: Unable to connect to AI service"}
    except Exception as err:
        print(f"Unexpected error occurred: {err}")
        return {"error": "Unexpected error: Unable to connect to AI service"}
