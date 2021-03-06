import requests
import json
import boto3
import datetime
from PIL import Image
import matplotlib.pyplot as plt

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
    now = (datetime.datetime.now()).strftime('%Y-%m-%d')
    # now = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    img = "https://ssf-graph-team2.s3.us-east-2.amazonaws.com/" + str(1) + "/" + now + ".png"

    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    data = { 'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({"object_type": "feed",
                                           "content": {"title": " 나문희 환자님의 "+now+"의 수면 그래프입니다", "description": "자세한 사항은 010-****-**** 으로 연락주세요",
                                                       "image_url": img,
                                                       "link": {"web_url": img}}})}

    response = requests.post(url, headers=headers, data=data)
    response.status_code

def crontab_job():
    send_talk()
    pass
send_talk()