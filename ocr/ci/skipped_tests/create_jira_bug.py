import sys
import requests
import os
from datetime import datetime

JIRA_URL = "https://imranslab.atlassian.net"
JIRA_API_ENDPOINT = "/rest/api/3/issue"
JIRA_EPIC_KEY = "OCR-6"
JIRA_PROJECT_KEY = "OCR"
JIRA_ISSUE_TYPE = "Bug"
JIRA_USER = os.environ.get("JIRA_USER")
JIRA_TOKEN = os.environ.get("JIRA_TOKEN")


def create_jira_issue(summary, description):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "issuetype": {"name": JIRA_ISSUE_TYPE},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{
                        "type": "text",
                        "text": description
                    }]
                }]
            },
            "customfield_10014": JIRA_EPIC_KEY,  # Epic Link
            "labels": ["automated", "ci-cd", "tests"],
            "priority": {"name": "Medium"}
        }
    }

    try:
        response = requests.post(
            f"{JIRA_URL}{JIRA_API_ENDPOINT}",
            json=payload,
            auth=(JIRA_USER, JIRA_TOKEN),
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️ Jira API Error: {str(e)}")
        if 'response' in locals():
            print(f"Response: {response.text}")
        return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python create_jira_bug.py <skipped_tests_file>")
        sys.exit(1)

    skipped_file = sys.argv[1]

    try:
        with open(skipped_file, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"❌ File not found: {skipped_file}")
        sys.exit(1)

    if "No skipped tests" in content:
        print("✅ No skipped tests to report")
        sys.exit(0)

    summary = f"[Automated] Skipped Tests - {datetime.utcnow().strftime('%Y-%m-%d')}"
    description = f"""*Automated Test Report*

    {{
        "type": "codeBlock",
        "content": [
            {{
                "type": "text",
                "text": "{content}"
            }}
        ]
    }}"""

    print(f"📨 Creating Jira issue for {os.path.basename(skipped_file)}")
    result = create_jira_issue(summary, description)

    if result:
        print(f"🎉 Created issue: {result.get('key')}")
        print(f"🔗 {JIRA_URL}/browse/{result.get('key')}")
    else:
        print("❌ Failed to create Jira issue")
        sys.exit(1)

if __name__ == "__main__":
    main()