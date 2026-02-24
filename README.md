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

> **Wichtig:** Lege deinen API-Key **nur** in der `.env`-Datei ab, niemals direkt im Code oder in Commits.

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

Stelle sicher, dass deine virtuelle Umgebung aktiv ist (`(venv)` im Terminal zu sehen) und führe dann aus:

```bash
source venv/bin/activate  # falls noch nicht aktiv
python app.py
```

Die Anwendung läuft dann standardmäßig unter:

- http://127.0.0.1:5000

Öffne die URL im Browser, gib oben im Feld eine Frage ein und klicke auf **Senden** – die Antwort der AI erscheint im Antwortbereich unterhalb.

---

## Projektstruktur

```text
AI-APP/
├─ app.py              # Flask-App mit Weboberfläche & Gemini-Anbindung
├─ main.py             # Einfaches Testskript für Gemini (optional)
├─ .env                # Enthält deinen GOOGLE_API_KEY (nicht im Git)
├─ .gitignore          # Ignoriert venv, .env etc.
├─ static/
│  └─ style.css        # Styling der Webseite mit Roboter-UI
└─ templates/
   └─ index.html       # HTML-Template für die Chat-Oberfläche
```

---

## Entwicklung & Anpassung

- **Layout anpassen:** Styles in `static/style.css`
- **HTML-Struktur ändern:** Template in `templates/index.html`
- **AI-Logik anpassen:** Route und Modell-Aufruf in `app.py`

Wenn du ein anderes Modell (z.B. `gemini-3.0` oder ähnliches) verwenden möchtest, kannst du es in `app.py` im Aufruf von `client.models.generate_content` ändern.

---

## Git & Deployment-Hinweise

### Ersten Commit erstellen

```bash
cd ~/Desktop/AI-APP
git add app.py main.py templates static .gitignore README.md
git commit -m "Initialer AI-Chat-Roboter"
```

### Branch auf `main` umbenennen und nach GitHub pushen

```bash
git branch -M main
git remote set-url origin https://github.com/SunnyDevZH/AI-Chat-Roboter.git
# oder, falls noch kein origin existiert
# git remote add origin https://github.com/SunnyDevZH/AI-Chat-Roboter.git

git push -u origin main
```

---

## Sicherheit

- API-Keys niemals im Code oder in Commits speichern.
- `.env` immer in `.gitignore` lassen.
- Wenn ein Key versehentlich veröffentlicht wurde, rotiere ihn im Google Cloud / Gemini Dashboard.

---

Viel Spaß mit deinem AI-Chat-Roboter 🤖 Wenn du möchtest, können wir als nächstes einen kleinen Chat-Verlauf, Theme-Switch (Hell/Dunkel) oder eine Mehrsprachen-Unterstützung einbauen.
