FROM python:3.9-slim

WORKDIR /app

# Kopiramo fajlove u kontejner
COPY . .

# Instaliramo Python zavisnosti
RUN pip install --no-cache-dir -r requirements.txt

# Pokrećemo Flask aplikaciju
CMD ["python", "app.py"]
