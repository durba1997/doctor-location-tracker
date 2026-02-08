import requests
import time
import random

DOCTOR_ID = "doctor_1"  # Change for each doctor
URL = "http://127.0.0.1:5000/update_location"

while True:
    # Replace these with real GPS in a real app
    lat = 19.0 + random.random()
    lon = 72.8 + random.random()
    
    payload = {"doctor_id": DOCTOR_ID, "lat": lat, "lon": lon}
    try:
        requests.post(URL, json=payload)
    except Exception as e:
        print("Error:", e)
    time.sleep(3)  # Send updates every 3 seconds
