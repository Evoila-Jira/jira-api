import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Jira-Zugangsdaten
jira_domain = "https://copitos.atlassian.net"
JIRA_EMAIL = "ocaylak@evoila.com"
JIRA_API_TOKEN = "ATATT3xFfGF0Pka2q0FqGWHcPmA0AxVyVe9V4P-ePCNm_tiMeP1tH_mR3i7NyTOZ1nv2MBd_KaxsH6a34P20tXf3D2ZdjCXhQOJiYyS0mNKdDITNLfLl_ge3eVac4veF1Z2E20zQCOPLaUGK1Ctm_7RPlD_oxJ-N_FAEpT4ka1hpCZPWAhL1Lmo=AE47B170"

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
