import requests
import json
from typing import Dict
from .config import get_jira_config

class JiraClient:
    """A Python package for Jira integration to create issues with test data."""

    def __init__(self):
        config = get_jira_config()
        self.base_url = config["base_url"]
        self.email = config["email"]
        self.api_token = config["api_token"]
        self.project_key = config["project_key"]
        self.auth = (self.email, self.api_token)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def create_issue(self, summary: str, payload: Dict):
        """Creates a Jira issue with test results as a payload."""
        url = f"{self.base_url}/rest/api/3/issue"
        issue_data = {
            "fields": {
                "project": {"key": self.project_key},
                "summary": summary,
                "description": json.dumps(payload, indent=4),
                "issuetype": {"name": "Bug"}  # Use valid issue type
            }
        }

        try:
            response = requests.post(
                url,
                headers=self.headers,
                auth=self.auth,
                data=json.dumps(issue_data),
                timeout=10
            )
            response.raise_for_status()

            if response.status_code == 201:
                issue_key = response.json()['key']
                print(f"✅ Jira Issue Created: {self.base_url}/browse/{issue_key}")
                return issue_key
            return None

        except requests.exceptions.HTTPError as err:
            print(f"❌ Jira API Error: {err}")
            print(f"Response Content: {response.text}")
            return None
        except Exception as err:
            print(f"❌ Unexpected Error: {err}")
            return None


    def get_issues(self, jql_query: str, fields: list = ["key", "summary", "issuetype"]) -> list:
        """Retrieve issues matching a JQL query."""
        try:
            url = f"{self.base_url}/rest/api/3/search"
            params = {
                "jql": jql_query,
                "fields": ",".join(fields),
                "maxResults": 50
            }

            response = requests.get(
                url,
                headers=self.headers,
                auth=self.auth,
                params=params,
                timeout=10
            )
            response.raise_for_status()

            return response.json().get("issues", [])

        except requests.exceptions.HTTPError as err:
            print(f"❌ Jira API Error: {err}\nResponse: {response.text}")
        except Exception as err:
            print(f"❌ Unexpected Error: {err}")

        return []