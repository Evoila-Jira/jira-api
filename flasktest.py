from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/jira-event', methods=['GET'])
def jira_event():
    issue_key = request.args.get('issueKey', 'Kein Key')
    summary = request.args.get('summary', 'Keine Zusammenfassung')

    return jsonify({
        "message": "GET-Anfrage empfangen",
        "issueKey": issue_key,
        "summary": summary
    })
pip install flask requests python-dotenv

if __name__ == '__main__':
    app.run(port=5000)
