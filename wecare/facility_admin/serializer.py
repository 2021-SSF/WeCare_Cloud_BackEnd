from rest_framework import serializers

from facility_admin.models import Bed, Room, Facility, Adminster

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'name', 'location', 'number']


class AdminsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adminster
        fields = ['id', 'facility_id', 'password']

class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ['id', 'room_id', 'camera_id']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'facility_id', 'room_loc']



