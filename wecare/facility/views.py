from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from facility.models import Elders
from facility.serializer import EldersSerializer, DietSerializer
from facility_admin.models import Room, Bed
from facility_admin.serializer import RoomSerializer, BedSerializer


def facilityRoom_list(request, facility_id):  # 병원 정보 페이지 리스트
    facilityRooms = Room.objects.filter(facility_id=facility_id)  # 시설 id에 맞는 room 리스트 가져오기
    serializer = RoomSerializer(facilityRooms, many=True)
    return Response(serializer.data)


def facility_detail(request, room_id):  # 병원정보 클릭하면 이동하는 페이지  # !!!!!!이부분은 나중에 변경 !!!!!
    beds = Bed.objects.filter(room_id=room_id)
    serializer = BedSerializer(beds, many=True)
    return Response(serializer.data)


def elders_add(request):  # 환자 추가 모달창
    serializer = EldersSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"})

    else:
        return Response({"message": "failed"})


def diet_add(request):  # 식단 추가 모달창
    serializer = DietSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"})

    else:
        return Response({"message": "failed"})


def elders_detail(request, elders_id):  # 환자 상세정보
    elders = Elders.objects.get(id=elders_id)
    serializer = EldersSerializer(elders, many=False)
    return Response(serializer.data)


def elders_update(request, elders_id):  # 환자 정보 수정
    elders = Elders.objects.get(id=elders_id)
    serializer = EldersSerializer(instance=elders, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Updated!"})
    else:
        return Response({"message": "Failed to update!"})


def elders_delete(request, elders_id):  # 환자 정보 삭제
    elders = Elders.objects.get(id=elders_id)
    elders.delete()
    return Response({"message": "Deleted!"})


from django.shortcuts import render

# Create your views here.
