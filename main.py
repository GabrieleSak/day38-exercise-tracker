import requests as requests
from auth import *

APP_ID = app_id
API_KEY = api_key

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": input("What exercise you did today? "),
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 172,
    "age": 30
}

response = requests.post(nutritionix_endpoint, json=params, headers=headers)
result = response.text
print(result)
