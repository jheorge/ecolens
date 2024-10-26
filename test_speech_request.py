import requests
import os

# Endpoint URL
url = 'http://localhost:5000/speech' 

payload = {
    'text': 'Hola, ¿cómo estás?'
}

response = requests.post(url, json=payload)
print(response.text)    