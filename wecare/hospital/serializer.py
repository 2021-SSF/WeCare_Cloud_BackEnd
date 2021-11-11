from rest_framework import serializers

from hospital.models import Patient, Nurse, Diet


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'nurse_id', 'bed_id', 'name', 'age', 'gender', 'note', 'companion_num', 'companion_relation']


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['id', 'admin_id', 'name', 'password', 'phone']


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = ['id', 'nurse_id', 'image', 'time']

