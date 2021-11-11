from rest_framework import serializers

from hospital_admin.models import Bed, Room


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ['id', 'room_id', 'camera_id']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hospital_id', 'room_loc']



