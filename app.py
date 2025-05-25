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

JIRA_EMAIL = os.getenv('JIRA_EMAIL')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')

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
