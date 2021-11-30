from rest_framework import serializers

from facility.models import Elder, Bed, Room, ElderStatus, Violence


class ElderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elder
        fields = ['id', 'room_id', 'bed_id', 'name', 'age', 'gender', 'sickness', 'recent_problem']



class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ['id', 'room_id']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_loc']


class ElderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElderStatus
        fields = ['id', 'elder_id', 'time', 'lay', 'sit', 'empty', 'recent_status', 'today_status', 'max_status']


class ElderStatusPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElderStatus
        fields = ['id', 'elder_id', 'time','today_status']



class ViolenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violence
        fields = ['id', 'bed_id', 'time']