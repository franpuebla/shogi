"""Rest Client for chat-bot-api"""
import requests
import re
import json

class Chatbotapi(object):
    "REST class"
    def __init__(self, uri, user, password):
        "Constructor"
        self.uri = uri
        self.api_version = '/0.1'
        self.password = password
        self.username = user
        self.path_separator = '/'

    def get(self, endpoint):
        "Simple GET"
        try:
            response = requests.get(
            "http://"+self.uri + self.api_version + endpoint,
            auth=(self.username, self.password),
            verify=False
            )
            if response.status_code == 200:
                data = json.loads(response.text)
            else:
                data = {}
            return data
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError()

    def post(self, endpoint, data):
        headers = { "Content-Type": "application/json" }
        try:
            response = requests.post(
                "http://"+self.uri + self.api_version + endpoint,
                auth=(self.username, self.password),
                verify=False,
                data=json.dumps(data),
                headers=headers
            )
            if response.status_code == 201:
                data = response.text
            else:
                data = {}
            return data
        except requests.exceptions.ConnectionError:
           raise requests.exceptions.ConnectionError()


class Waboxapp(object):
    "REST class"
    def __init__(self, uri):
        "Constructor"
        self.uri = uri
        self.path_separator = '/'

    def get(self, endpoint):
        "Simple GET"
        try:
            response = requests.get(
            "https://"+self.uri + endpoint,
            verify=False
            )
            if response.status_code == 200:
                data = json.loads(response.text)
            else:
                data = {}
            return data
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError()

    def post(self, endpoint, data):
        headers = { "Content-Type": "application/json" }
        try:
            response = requests.post(
                "https://"+self.uri+ endpoint,
                verify=False,
                data=json.dumps(data),
                headers=headers
            )
            if response.status_code == 200:
                data = response.text
            else:
                data = {}
            return data
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError()
