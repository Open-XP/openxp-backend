# Service.py
import requests
from django.conf import settings

def call_ai_api(prompt):
    # api_url = 'https://api.aimlapi.com/chat/completions'
    api_url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.AI71_API_KEY}'  # Use f-string for interpolation
    }
    data = {
        "model": "gpt-4o-mini",
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
        # "max_tokens": 500,  # Increased for more detailed responses
        # "temperature": 0.6,  # Slightly lower for more focused responses
        # "frequency_penalty": 0.8,  # Lowered slightly to allow some repetition
        # "presence_penalty": 0.6,  # Increased for introducing new topics
        # "top_p": 0.95,  # Increased for more diverse outputs
        # "top_k": 40,  # Lowered to make the model consider fewer tokens for more coherent output
        # "n": 1,
        # "stop": ["career", "topic", "question", "education"]  # Stop tokens remain the same
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
    # api_url = 'https://api.aimlapi.com/chat/completions'
    api_url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.AI71_API_KEY}'
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "max_tokens": 1000 
    }
    
    print('Data sent to API:', data)

    try:
        response = requests.post(api_url, json=data, headers=headers, timeout=60)
        response.raise_for_status()
        
        # Print full response for debugging
        print('Response status code:', response.status_code)
        print('Response headers:', response.headers)
        print('Response text:', response.text)
        
        json_response = response.json()
        
        # Adjust this based on the actual structure of the API response
        generated_text = json_response['choices'][0]['message']['content']
        
        return generated_text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except ValueError:
        return {"error": "Invalid response from AI service"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}
