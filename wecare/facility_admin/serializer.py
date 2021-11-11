from rest_framework import serializers

from facility_admin.models import Bed, Room


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ['id', 'room_id', 'camera_id']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'facility_id', 'room_loc']



