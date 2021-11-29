import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import boto3
from botocore.exceptions import ClientError
import logging

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from facility.models import ElderStatus,Elder
from facility.serializer import ElderStatusSerializer,ElderSerializer
from collections import OrderedDict
import datetime

#ssf-graph-team2우리 이미지 bucket 이름

def draw_one_patient():
    draw_graph_elder(1)

def draw_all():
    draw_graph_all_elders()

def draw_graph_all_elders():
    elders = Elder.objects.all()
    elders_serializer = ElderSerializer(elders, many=True)
    for data in elders_serializer.data:
        draw_graph_elder(dict(data)['id'])

def draw_graph_elder(id):
    elder = ElderStatus.objects.filter(elder_id=id)
    serializer = ElderStatusSerializer(elder, many=True)

    chat_st = {}

    for data in serializer.data:
        data_re = dict(data)
        if data_re['today_status'] == "empty":
            chat_st[data_re['time']] = 0
        if data_re['today_status'] == "sit":
            chat_st[data_re['time']] = 1
        if data_re['today_status'] == "lay":
            chat_st[data_re['time']] = 2

    x_st = chat_st.keys()
    y_st = chat_st.values()

    plt.plot(x_st, y_st)
    plt.xlabel('time')
    plt.ylabel('status')

    now = datetime.datetime.now().strftime('%Y-%m-%d')

    plt.savefig(now)
    upload = now + '.png'

    upload_graph(upload, 'ssf-graph-team2', str(id))


    os.remove(upload)


def upload_graph(file_name, bucket,id, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

        # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, '%s/%s' % (id, file_name))
    except ClientError as e:
        logging.error(e)
        return False
    return True

