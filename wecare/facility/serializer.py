from rest_framework import serializers

from facility.models import Elders, Nurse, Diet


class EldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elders
        fields = ['id', 'nurse_id', 'bed_id', 'name', 'age', 'gender', 'note', 'companion_num', 'companion_relation']


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['id', 'admin_id', 'name', 'password', 'phone']


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = ['id', 'nurse_id', 'image', 'time']

