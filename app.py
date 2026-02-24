from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Configure AI API
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            # Generate AI response using updated library
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )
            response_text = response.text
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)