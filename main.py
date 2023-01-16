import requests as requests
from auth import *
from datetime import datetime

APP_ID = app_id
API_KEY = api_key
SHEET_TOKEN = sheet_token

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheet_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

params = {
    "query": input("What exercise you did today? "),
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 172,
    "age": 30
}

response = requests.post(nutritionix_endpoint, json=params, headers=headers)
result = response.json()

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheet_headers)

print(sheet_response.text)
