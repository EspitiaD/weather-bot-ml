# 🤖 Weather Bot con Machine Learning

Este proyecto es un bot de predicción del clima que combina datos meteorológicos reales de una API con un modelo de Machine Learning. Usa información actual del clima (como temperatura, humedad, presión, etc.) para predecir la probabilidad de lluvia u otras condiciones.

## 🌐 ¿Qué hace este bot?

1. Consulta los datos del clima actual usando una API gratuita.
2. Usa un modelo de Machine Learning (`RandomForestClassifier`) entrenado con datos reales para predecir si lloverá o no.
3. Muestra la predicción junto con el clima actual en consola.
4. (Opcional) Genera gráficos de correlación entre variables climáticas.

## 🚀 Cómo instalar y correr

1. Clona el repositorio:

```bash
git clone https://github.com/EspitiaD/weather-bot-ml.git
cd weather-bot-ml

Crea un entorno virtual y actívalo:

python3 -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate

Instala las dependencias:

pip install -r requirements.txt

Ejecuta el bot:

python clima_ml.py

🧪 Ejemplo de salida

🌡️  Clima en vivo:
Temperatura: 15.1°C
Humedad: 91%
Presión: 1015.5 hPa
Precipitación: 0.00 mm

🤖 Predicción ML:
¿Lloverá mañana?: No

📦 Requisitos

Revisa el archivo requirements.txt para ver las librerías utilizadas.

📌 Autor
Creado por EspitiaD como proyecto educativo para aprender Python, APIs y Machine Learning.
