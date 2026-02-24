import os
from dotenv import load_dotenv
from google.genai import Client

# .env laden
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Client initialisieren
client = Client(api_key=api_key)

# Inhalt, den du an die AI schicken willst
prompt = "Welche Farbe hat ein Apfel?"

# Anfrage an das Modell
response = client.models.generate_content(
    model="gemini-2.5-flash",    # falls dieser im kostenlosen Bereich verfügbar ist
    contents=prompt
)

print("Antwort:", response.text)