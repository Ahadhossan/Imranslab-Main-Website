import os

def get_jira_config():
    """Retrieve Jira configuration from environment variables."""
    return {
        "base_url": os.getenv("JIRA_BASE_URL", "https://imranslab.atlassian.net"),
        "email": os.getenv("JIRA_EMAIL"),
        "api_token": os.getenv("JIRA_API_TOKEN"),
        "project_key": os.getenv("JIRA_PROJECT_KEY", "BR"),
    }
