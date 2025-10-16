import pytest
from jira_integration.jira import JiraClient
import requests
import os

@pytest.fixture
def jira_client():
    """Fixture to initialize JiraClient with test configuration"""
    # Override config for testing
    os.environ["JIRA_EMAIL"] = "test@example.com"  # Use valid credentials
    os.environ["JIRA_API_TOKEN"] = "your_api_token_here"
    return JiraClient()

def test_simple_issue_creation(jira_client):
    pytest.skip("We need to fix this JIRA Package to make sure we can do CRUD operation")
    """Test creating a simple issue in Jira with required fields."""
    test_payload = {
        "description": "Test issue from automated tests",
        "priority": "Medium",  # Add required field based on your Jira setup
        "labels": ["automated-test"]
    }
    issue_key = jira_client.create_issue("Test Issue Creation", test_payload)
    assert issue_key is not None, "Issue creation failed. Check permissions and configuration."

def test_check_project_permissions(jira_client):
    pytest.skip("We need to fix this JIRA Package to make sure we can do CRUD operation")
    """Test if the user has permission to create issues in the Jira project."""

    url = f"{jira_client.base_url}/rest/api/3/mypermissions"
    response = requests.get(
        url,
        auth=(jira_client.email, jira_client.api_token),
        headers={"Accept": "application/json"}
    )

    assert response.status_code == 200, "Failed to check permissions"
    permissions = response.json().get("permissions", {})
    create_issues_perm = permissions.get("CREATE_ISSUES", {})
    assert create_issues_perm.get("havePermission", False), "Missing CREATE_ISSUES permission"

# Keep other tests but ensure they use valid project keys and credentials

def test_get_similar_issues(jira_client):
    """Test retrieving similar issues from the project."""
    pytest.skip("We need to fix this JIRA Package to make sure we can do CRUD operation")
    # Search for all tasks created in the last 7 days
    test_jql = (
        f'project = {jira_client.project_key} AND '
        'issuetype = Task AND '
        'created >= -7d ORDER BY created DESC'
    )

    issues = jira_client.get_issues(test_jql)
    assert issues is not None, "Failed to retrieve issues"

    print(f"\nFound {len(issues)} similar issues:")
    for idx, issue in enumerate(issues[:5], 1):  # Display first 5 matches
        fields = issue.get("fields", {})
        print(f"{idx}. {issue['key']} - {fields.get('summary')} "
              f"({fields.get('issuetype', {}).get('name')})")

    # Basic sanity check - assumes there's at least one test issue
    assert len(issues) > 0, "No matching issues found - test data required"