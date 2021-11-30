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

tokens={'access_token': 'qPaUMDAr1-myuMv8Et3VPbkQeMsl-hCTVCjPTQo9dRkAAAF9b7tC3w', 'token_type': 'bearer', 'refresh_token': 'wl6wf7ZykqD4pRr77h-Zv-HMUskOxRBTjVBvcgo9dRkAAAF9b7tC3g', 'expires_in': 21599, 'scope': 'talk_message profile_nickname friends', 'refresh_token_expires_in': 5183999}

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
            "text": "폭행 발행!",
            "link": {
                url:""
            }
        })
    }

    response = requests.post(url, headers=headers, data=data)
    response.status_code
