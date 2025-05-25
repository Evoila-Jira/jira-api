import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()


# Jira-Zugangsdaten
jira_domain = "https://copitos.atlassian.net"
project_key = "COP"

JIRA_EMAIL = os.getenv('JIRA_EMAIL')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')

# JQL-Abfrage: offene Tickets im Projekt COP3
jql_query = f'project = {project_key} AND statusCategory = "In Progress"'

# API-Endpunkt
url = f"{jira_domain}/rest/api/3/search"

# Header und Parameter
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
params = {
    "jql": jql_query,
    "fields": "id"
}

# Anfrage senden
response = requests.get(url, headers=headers, params=params, auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN))

# Ergebnis auswerten
if response.status_code == 200:
    data = response.json()
    print(f"Offene Tickets in {project_key}: {data['total']}")
else:
    print(f"Fehler: {response.status_code}")
    print(response.text)
