import requests
import json

API_KEY = "tYvBkdiiJEVQ"
PROJECT_TOKEN = "tTJVZUWJFGGq"
RUN_TOKEN = "tWX1Tu2g9JAW"

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
data = json.loads(response.text)

class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }