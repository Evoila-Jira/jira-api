from flask import Flask, request, jsonify
import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

JIRA_URL = 'https://copitos.atlassian.net'
PROJECT_KEY = 'COP'
ISSUE_TYPE = '[System] Service request'
CUSTOM_FIELD_ID = 'customfield_10226'

JIRA_EMAIL = "ocaylak@evoila.com"
JIRA_API_TOKEN = "ATATT3xFfGF0M1ab2Np1AH2XvA8hkB8nIPeENZDMiRayfYZT_hpOwJdKZwbaXyuuybWO4AtP-C4TB8mma0LrTrwNURpRbHyAfzJk8STraXcLlVRMf-xugfGcLk75kXDutD37vkkyJDfO-GZqJtDlt6GS2U-1WdJdbL1jEcw29jKIRkTj9Ovqi-U=937CF889"  # <-- hier dein Token einsetzen

@app.route('/create-ticket', methods=['POST'])
def create_ticket():
    data = request.get_json()
    summary = data.get('summary')
    description = data.get('description')
    user = data.get('user')

    issue_data = {
        "fields": {
            "project": { "key": PROJECT_KEY },
            "summary": summary,
            "description": description,
            "issuetype": { "name": ISSUE_TYPE },
            CUSTOM_FIELD_ID: user
        }
    }

    response = requests.post(
        f"{JIRA_URL}/rest/api/3/issue",
        json=issue_data,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    )

    if response.status_code == 201:
        return jsonify({ "message": "Ticket erstellt", "key": response.json().get("key") }), 201
    else:
        return jsonify({ "error": response.json() }), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
