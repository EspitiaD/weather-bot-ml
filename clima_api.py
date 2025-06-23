import requests

# Coordenadas de Cali, Colombia
lat = 3.4516
lon = -76.5320

# URL de Open-Meteo (clima actual + predicción diaria)
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={lat}&longitude={lon}"
    f"&current=temperature_2m,relative_humidity_2m,pressure_msl,precipitation,weather_code"
    f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code"
    f"&timezone=auto"
)

# Obtener datos desde la API
respuesta = requests.get(url)
datos = respuesta.json()

# ============================
# 🌍 CLIMA EN VIVO EN CALI
# ============================
actual = datos["current"]

print("\n🌍 CLIMA EN VIVO EN CALI:")
print(f"Hora local: {actual['time']}")
print(f"Temperatura actual: {actual['temperature_2m']} °C")
print(f"Humedad: {actual['relative_humidity_2m']} %")
print(f"Presión: {actual['pressure_msl']} hPa")
print(f"Precipitación actual: {actual['precipitation']} mm")

# Lógica para saber si está lloviendo ahora
if actual["precipitation"] > 0:
    print("👉 Está lloviendo en este momento ☔")
else:
    print("👉 No está lloviendo ahora mismo 🌤️")

# ============================
# 📅 PRONÓSTICO PARA MAÑANA
# ============================
manana = {
    "max_temp": datos["daily"]["temperature_2m_max"][1],
    "min_temp": datos["daily"]["temperature_2m_min"][1],
    "lluvia": datos["daily"]["precipitation_sum"][1],
    "codigo": datos["daily"]["weather_code"][1],
}

# Interpretación de códigos del clima
codigo_clima = {
    0: "Despejado",
    1: "Mayormente despejado",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Niebla",
    48: "Niebla con escarcha",
    51: "Llovizna ligera",
    61: "Lluvia ligera",
    63: "Lluvia moderada",
    65: "Lluvia fuerte",
    71: "Nieve ligera",
    80: "Chubascos ligeros",
    95: "Tormenta",
}
descripcion = codigo_clima.get(manana["codigo"], "Condición desconocida")

print("\n📅 PRONÓSTICO PARA MAÑANA:")
print(f"Temperatura máxima: {manana['max_temp']} °C")
print(f"Temperatura mínima: {manana['min_temp']} °C")
print(f"Lluvia estimada: {manana['lluvia']} mm")
print(f"Condición probable: {descripcion}")
