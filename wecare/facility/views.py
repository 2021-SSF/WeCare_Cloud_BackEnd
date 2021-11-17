from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from facility.models import Room, Elder, ElderStatus
from facility.serializer import RoomSerializer, ElderSerializer, ElderStatusSerializer


@api_view(['GET'])
def facilityRoom_list(request):  # 병원 정보 페이지 리스트
    facilityRooms = Room.objects.all()
    serializer = RoomSerializer(facilityRooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def facility_detail(request, room_id):  # 병원정보 클릭하면 이동하는 페이지  # !!!!!!이부분은 나중에 변경 !!!!!
    elders = Elder.objects.filter(room_id=room_id)
    serializer = ElderSerializer(elders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def elder_detail(request, elders_id):  # 환자 상세정보
    elders = Elder.objects.get(id=elders_id)
    serializer = ElderSerializer(elders, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def elderStatus_Create(request):
    serializer = ElderStatusSerializer(request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"})

    else:
        return Response({"message": "failed"})
