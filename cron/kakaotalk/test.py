import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'd153e14bfad1b0d801b8533eb34bc37b'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'u2583Kya1x1TxnBsQHR4SKzVx_2PY7iqKHuteFkdy8crbDOiqLHK18PvoptTFM7ISdAAwgo9dZsAAAF9NtwKLw'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("../json/kakao_code.json", "r") as fp:
    json.dump(tokens, fp)

