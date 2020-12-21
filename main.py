import requests
import json
import pyttsx3
import speech_recognition as sr
import re

API_KEY = "tYvBkdiiJEVQ"
PROJECT_TOKEN = "tTJVZUWJFGGq"
RUN_TOKEN = "tWX1Tu2g9JAW"



class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
        self.data = json.loads(response.text)

    def get_total_cases(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']

    def get_total_deaths(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Deaths:":
                return content['value']

    def get_total_recovered(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Recovered:":
                return content['value']

        return "0"

    def get_country_data(self, country):
        data = self.data['country']

        for content in data:
            if content['name'].lower() == country.lower():
                return content

        return "0"
    

data = Data(API_KEY, PROJECT_TOKEN)
print(data.get_country_data('usa')['total_cases'])

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndwait()

speak("Hello")