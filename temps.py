import requests
import json
from datetime import datetime

# ---------------------
# CONFIGURACIÓ
# ---------------------
CIUTAT = "Barcelona"  # Pots canviar-ho
LAT = 41.3851
LON = 2.1734

# ---------------------
# OBTE TEMPERATURES
# ---------------------
# API d'Open-Meteo per obtenir temperatures horàries
url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&hourly=temperature_2m&timezone=Europe%2FMadrid"

response = requests.get(url)
data = response.json()

temperatures = data['hourly']['temperature_2m']

# ---------------------
# CALCULS
# ---------------------
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

# ---------------------
# EXPORTAR A JSON
# ---------------------
nom_fitxer = f"temp_{datetime.now().strftime('%Y%m%d')}.json"
with open(nom_fitxer, "w") as f:
    json.dump(resultat, f, indent=4)

print(f"Dades guardades a {nom_fitxer}")