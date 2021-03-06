import json

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from facility.models import Room, Elder, ElderStatus, Violence,Bed
from facility.serializer import RoomSerializer, ElderSerializer, ElderStatusSerializer, ViolenceSerializer,BedSerializer,ElderStatusPutSerializer

from facility.kakao import send_talk

from django.db.models import Q


@api_view(['GET'])
def facility_room_list(request):  # 병원 정보 페이지 리스트
    facilityRooms = Room.objects.all()
    serializer = RoomSerializer(facilityRooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def facility_detail(request, room_id):  # 병원정보 클릭하면 이동하는 페이지  # !!!!!!이부분은 나중에 변경 !!!!!
    elders = Elder.objects.filter(room_id=room_id)
    serializer = ElderSerializer(elders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def elder_detail(request, elder_id):  # 환자 상세정보
    elders = Elder.objects.get(id=elder_id)
    serializer = ElderSerializer(elders, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def elder_status_update(request):
    data = json.loads(request.body)
    content = request.data
    serializer = ElderStatusPutSerializer(data=content)


    if serializer.is_valid():
        elder_statuses = ElderStatus.objects.filter(Q(elder_id=content["elder_id"]) & Q(time=content["time"]))

        if elder_statuses.exists():
            elder_status = elder_statuses[0]
            elder_status.today_status = data.get('today_status')
            elder_status.save()
            return Response({"message": "success"})
        # 만약 데이터가 없으면 생성할 코드 하나 만들자
        # else:
        #     elder_status_create(request)

    else:
        return Response({"message": "failed"})



@api_view(['GET'])
def elder_status_list(request, elder_id):
    elder_status = ElderStatus.objects.filter(elder_id=elder_id)

    serializer = ElderStatusSerializer(elder_status, many=True)
    # print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def incident_create(request):
    send_talk() #폭행 발생 카카오톡 보내기
    serializer = ViolenceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"})

    else:
        return Response({"message": "failed"})


@api_view(['GET'])
def incident_list(request, room_id):
    bed = Bed.objects.filter(room_id=room_id)

    violence = Violence.objects.filter(bed_id_id__in=bed)
    serializer = ViolenceSerializer(violence, many=True)
    return Response(serializer.data)





