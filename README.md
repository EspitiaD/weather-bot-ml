# 🤖 Weather Bot con Machine Learning

Este proyecto es un bot de predicción del clima que combina datos meteorológicos reales de una API con un modelo de Machine Learning. Usa información actual del clima (como temperatura, humedad, presión, etc.) para predecir la probabilidad de lluvia u otras condiciones.

## 🌐 ¿Qué hace este bot?

- Obtiene **datos del clima en tiempo real** (temperatura, humedad, presión, etc.) desde una API pública.
- Procesa estos datos y predice si **lloverá próximamente** usando un modelo entrenado.
- Visualiza relaciones entre variables con gráficos (opcional).
- Es una base para futuros bots más complejos (clima por ciudad, predicción avanzada, alarmas, etc.).

- ## 🛠️ Tecnologías utilizadas

- Python 3.x  
- Pandas  
- Scikit-learn  
- Requests  
- Matplotlib / Seaborn  
- API de Open-Meteo.org

- ## 🧠 ¿Qué aprendí con este proyecto?

- Cómo funciona el ciclo básico del Machine Learning: recolección → entrenamiento → predicción.
- Cómo usar una API real para obtener datos en vivo.
- Procesamiento de datos con Pandas.
- Entrenamiento de modelos con Scikit-learn.
- Generación de visualizaciones y exportación de predicciones.

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

📬 Contacto
Si te interesa colaborar, proponer mejoras o contratar desarrollo de soluciones con IA:
www.linkedin.com/in/espitiad

![Vista previa del bot](https://raw.githubusercontent.com/EspitiaD/weather-bot-ml/main/correlaciones_clima.png)

