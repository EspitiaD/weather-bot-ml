# weather-bot-ml
# Bot de predicción climática con Python

Este proyecto utiliza un modelo de Machine Learning para predecir si lloverá o no, basándose en datos atmosféricos (temperatura, presión, humedad, etc.).

🔧 Herramientas usadas:
- Python
- Pandas
- Scikit-learn
- API de clima

💡 Aplicación: Este proyecto puede extenderse a predicciones más complejas o integrarse con sensores reales en zonas rurales.

✅ Estado: Funcional, con datos de prueba. En desarrollo para integración en tiempo real.

Pasos para correr el proyecto:
Clona este repositorio y entra a la carpeta:
git clone https://github.com/EspitiaD/weather-bot-ml.git && cd weather-bot-ml

Crea un entorno virtual e instálalo:
python3 -m venv venv && source venv/bin/activate
(En Windows: venv\Scripts\activate.bat)

Instala las dependencias necesarias:
pip install -r requirements.txt

Ejecuta el script del bot:
python clima_ml.py

El bot entrenará un modelo para predecir lluvia con base en datos climáticos. Mostrará la precisión del modelo, una predicción con datos de ejemplo y un gráfico de correlaciones entre variables.
