import requests
import json
import time
from datetime import datetime

CIUTAT = "Barcelona"
LAT = 41.3851
LON = 2.1734

url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&hourly=temperature_2m&timezone=Europe%2FMadrid"

for intent in range(3):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        break
    except requests.exceptions.RequestException as e:
        print(f"Intent {intent+1} fallit: {e}")
        if intent < 2:
            time.sleep(10)
        else:
            raise

temperatures = data["hourly"]["temperature_2m"]

temp_max = max(temperatures)
temp_min = min(temperatures)
temp_mitjana = sum(temperatures) / len(temperatures)

resultat = {
    "ciutat": CIUTAT,
    "data": datetime.now().strftime("%Y-%m-%d"),
    "temperatura_max": temp_max,
    "temperatura_min": temp_min,
    "temperatura_mitjana": temp_mitjana
}

nom_fitxer = f"temp_{datetime.now().strftime('%Y%m%d')}.json"

with open(nom_fitxer, "w", encoding="utf-8") as f:
    json.dump(resultat, f, indent=4)

print(f"Dades guardades a {nom_fitxer}")