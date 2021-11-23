from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from facility.models import Room, Elder, ElderStatus, Violence,Bed
from facility.serializer import RoomSerializer, ElderSerializer, ElderStatusSerializer, ViolenceSerializer,BedSerializer

from facility.kakao import send_talk

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


@api_view(['POST'])
def elder_status_create(request):
    serializer = ElderStatusSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"})

    else:
        return Response({"message": "failed"})


@api_view(['GET'])
def elder_status_list(request, elder_id):
    elder_status = ElderStatus.objects.get(elder_id=elder_id)

    serializer = ElderStatusSerializer(elder_status,many=True)
    print(serializer.data)
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





