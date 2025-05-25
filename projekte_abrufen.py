import requests

from flask import Flask
app = Flask(__name__)


# Deine ngrok-URL
url = "https://4cc6-104-151-118-50.ngrok-free.app/projects"

print("🔄 Lade Projekte von Flask-Server...")

try:
    response = requests.get(url)
    response.raise_for_status()
    projects = response.json()

    print(f"✅ {len(projects)} Projekte gefunden:\n")
    for project in projects:
        print(f"🔹 {project['key']}: {project['name']}")
except Exception as e:
    print(f"❌ Fehler beim Abrufen der Projekte: {e}")
