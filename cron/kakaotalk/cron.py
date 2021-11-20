import requests
import json
import boto3
import datetime
from PIL import Image

with open("../json/kakao_code.json", "r") as fp:
    tokens = json.load(fp)

def get_graph():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('ssf-graph-team2')
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    # 만약 실제로 돌릴거면 d -1일 해야함
    object = bucket.Object(now+'.png')
    response = object.get()
    file_stream = response['Body']
    img = Image.open(file_stream)
    return img


def send_talk():
    graph = get_graph()
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": "Hello, world!",
            "link": {
                "web_url": "www.naver.com"
            }
        })
    }
    response = requests.post(url, headers=headers, data=data)
    response.status_code