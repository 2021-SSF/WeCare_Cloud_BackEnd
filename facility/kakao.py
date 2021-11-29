import requests
import json
import boto3
import datetime
from PIL import Image
import os
# current_path = os.getcwd()

# file = os.path.join(os.getcwd()+"kakao_code.json")
# print(file)
# with open(file,"r") as fp:
#     tokens = json.load(fp)

tokens={"access_token": "토큰", 
        "token_type": "bearer", 
        "refresh_token": "토큰", 
        "expires_in": 21599, 
        "scope": "talk_message", 
        "refresh_token_expires_in": 5183999}

def send_talk():
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": "폭행 발행!",
            "link": {

            }
        })
    }

    response = requests.post(url, headers=headers, data=data)
    response.status_code
