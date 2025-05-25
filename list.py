import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Jira-Zugangsdaten
jira_domain = "https://copitos.atlassian.net"
JIRA_EMAIL = "ocaylak@evoila.com"
JIRA_API_TOKEN = "ATATT3xFfGF0M1ab2Np1AH2XvA8hkB8nIPeENZDMiRayfYZT_hpOwJdKZwbaXyuuybWO4AtP-C4TB8mma0LrTrwNURpRbHyAfzJk8STraXcLlVRMf-xugfGcLk75kXDutD37vkkyJDfO-GZqJtDlt6GS2U-1WdJdbL1jEcw29jKIRkTj9Ovqi-U=937CF889"

# API-Endpunkt
url = f"{jira_domain}/rest/api/3/project/search"

# Header
headers = {
    "Accept": "application/json"
}

print("🔄 Verbinde mit Jira Cloud...")

# Anfrage senden
response = requests.get(url, headers=headers, auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN))

# Ergebnis auswerten
if response.status_code == 200:
    projects = response.json().get("values", [])
    if not projects:
        print("⚠️ Keine Projekte gefunden. Möglicherweise fehlen Berechtigungen oder es gibt keine sichtbaren Projekte.")
    else:
        print(f"✅ {len(projects)} Projekte gefunden:\n")
        for project in projects:
            print(f"🔹 {project['key']}: {project['name']}")
else:
    print(f"❌ Fehler beim Abrufen der Projekte: HTTP {response.status_code}")
    try:
        print("Antwort von Jira:", response.json())
    except Exception:
        print("Antwort konnte nicht als JSON gelesen werden.")
        print(response.text)
