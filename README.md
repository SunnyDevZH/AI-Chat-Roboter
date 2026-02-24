# AI-Chat-Roboter

Ein kleiner, moderner Chat-Roboter auf Basis von Googles Gemini, gebaut mit Python und Flask. Du kannst dem Roboter Fragen stellen, und die Antwort der AI wird direkt in einer hübschen Weboberfläche angezeigt.

## Features

- 🧠 Anbindung an Googles Gemini (über `google-genai`)
- 🌐 Einfache Weboberfläche mit Flask
- 🤖 Kleiner Roboter als Header-Illustration
- 💬 Eingabefeld für Fragen + Antwortbereich
- 🔐 API-Key wird über `.env` verwaltet (nicht im Repo)

---

## Voraussetzungen

- Python 3.10+ (empfohlen)
- Git
- Ein Google Gemini API-Key

---

## Installation & Setup

1. Repository klonen (oder lokal in dieses Verzeichnis wechseln):

   ```bash
   cd ~/Desktop/AI-APP
   ```

2. Virtuelle Umgebung erstellen und aktivieren:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Benötigte Python-Pakete installieren:

   ```bash
   pip install flask google-generativeai google-genai python-dotenv
   ```

4. `.env`-Datei mit deinem API-Key anlegen (falls nicht schon vorhanden):

   ```env
   GOOGLE_API_KEY=dein_gemini_api_key_hier
   ```

   Die Datei `.env` ist bereits in `.gitignore` eingetragen und wird nicht zu GitHub hochgeladen.

---

## Anwendung starten

```bash
source venv/bin/activate  
python app.py
```

Die Anwendung läuft dann standardmäßig unter:

- http://127.0.0.1:5000

---

## Entwicklung & Anpassung

- **Layout anpassen:** Styles in `static/style.css`
- **HTML-Struktur ändern:** Template in `templates/index.html`
- **AI-Logik anpassen:** Route und Modell-Aufruf in `app.py`

Wenn du ein anderes Modell (z.B. `gemini-3.0` oder ähnliches) verwenden möchtest, kannst du es in `app.py` im Aufruf von `client.models.generate_content` ändern.




