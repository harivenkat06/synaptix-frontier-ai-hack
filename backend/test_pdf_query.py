import requests
import json

url = "http://localhost:8001/ask"
payload = {"query": "What is the annual leave policy?"}
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except Exception as e:
    print("Error:", e)
