from django.shortcuts import render


# Create your views here.
from rest_framework.response import Response

from hospital.models import Patient
from hospital.serializer import PatientSerializer, DietSerializer
from hospital_admin.models import Room, Bed
from hospital_admin.serializer import RoomSerializer, BedSerializer



def hospitalRoom_list(request, hospital_id):  # 병원 정보 페이지 리스트
    hospitalRooms = Room.objects.filter(hospital_id=hospital_id)  # 병원 id에 맞는 room 리스트 가져오기
    serializer = RoomSerializer(hospitalRooms, many=True)
    return Response(serializer.data)


def hospital_detail(request, room_id):  # 병원정보 클릭하면 이동하는 페이지  # !!!!!!이부분은 나중에 변경 !!!!!
    beds = Bed.objects.filter(room_id=room_id)
    serializer = BedSerializer(beds, many=True)
    return Response(serializer.data)


def patient_add(request):  # 환자 추가 모달창
    serializer = PatientSerializer(data=request.data)

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


def patient_detail(request, patient_id):  # 환자 상세정보
    patients = Patient.objects.get(id=patient_id)
    serializer = PatientSerializer(patients, many=False)
    return Response(serializer.data)


def patient_update(request, patient_id):  # 환자 정보 수정
    patients = Patient.objects.get(id=patient_id)
    serializer = PatientSerializer(instance=patients, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Updated!"})
    else:
        return Response({"message": "Failed to update!"})


def patient_delete(request, patient_id):  # 환자 정보 삭제
    patients = Patient.objects.get(id=patient_id)
    patients.delete()
    return Response({"message": "Deleted!"})
