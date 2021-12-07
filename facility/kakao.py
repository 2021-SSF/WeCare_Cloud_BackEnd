import requests
import json
import boto3
import datetime
from PIL import Image
import os
this_directory = os.path.dirname(__file__)
file_path = os.path.join(this_directory, '../kakao_json/kakao_json.json')

with open(file_path, "r") as fp:
    tokens = json.load(fp)

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"
headers={"Authorization" : "Bearer " + tokens["access_token"]}

result = json.loads(requests.get(friend_url, headers=headers).text)
friends_list = result.get("elements")
friend_id = friends_list[2].get("uuid")


def send_talk():
    url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    data = {
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type": "text",
            "text": "소란 발행!",
            "link": {
                url:""
            }
        })
    }

    response = requests.post(url, headers=headers, data=data)
    response.status_code
