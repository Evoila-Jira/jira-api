import requests

# Deine ngrok-URL
url = "https://70a9-104-151-118-50.ngrok-free.app/projects"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
