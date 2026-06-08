import json

import requests


def get_session_token(username: str, password: str):
    url = "https://www.easistent.com/m/login"

    payload = json.dumps({
    "username": username,
    "password": password,
    "supported_user_types": [
        "parent",
        "child",
        "parent_of_pre_enrolled"
    ]
    })
    headers = {
    'x-child-id': '662787',
    'x-client-platform': 'web',
    'x-client-version': '13',
    'x-app-name': 'null',
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if not response.ok:
        return None

    return response.json()["access_token"]["token"]


