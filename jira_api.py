from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# Jira-Zugangsdaten
JIRA_DOMAIN = "https://copitos.atlassian.net"
JIRA_EMAIL = "ocaylak@evoila.com"
JIRA_API_TOKEN = "ATATT3xFfGF0M1ab2Np1AH2XvA8hkB8nIPeENZDMiRayfYZT_hpOwJdKZwbaXyuuybWO4AtP-C4TB8mma0LrTrwNURpRbHyAfzJk8STraXcLlVRMf-xugfGcLk75kXDutD37vkkyJDfO-GZqJtDlt6GS2U-1WdJdbL1jEcw29jKIRkTj9Ovqi-U=937CF889"  # <-- hier dein Token einsetzen

# Endpunkt: Liste aller Projekte
@app.route("/projects", methods=["GET"])
def list_projects():
    url = f"{JIRA_DOMAIN}/rest/api/3/project/search"
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code == 200:
        projects = response.json().get("values", [])
        return jsonify([
            {"key": p["key"], "name": p["name"]} for p in projects
        ])
    else:
        return jsonify({"error": response.text}), response.status_code

# Endpunkt: Ticket erstellen
@app.route("/create-ticket", methods=["POST"])
def create_ticket():
    data = request.json
    project_key = data.get("project")
    summary = data.get("summary")
    description = data.get("description", "")

    if not project_key or not summary:
        return jsonify({"error": "project and summary are required"}), 400

    url = f"{JIRA_DOMAIN}/rest/api/3/issue"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"}  # ggf. anpassen für ITSM
        }
    }

    response = requests.post(url, json=payload, headers=headers, auth=auth)
    if response.status_code == 201:
        issue = response.json()
        return jsonify({
            "key": issue["key"],
            "url": f"{JIRA_DOMAIN}/browse/{issue['key']}"
        })
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(port=5000)
