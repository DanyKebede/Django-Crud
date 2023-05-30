from rest_framework import serializers
from .models import Hospital, Doctor

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'phone', 'address', 'image', 'latitude', 'longitude', 'rating', 'email', 'openhours')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'age', 'hospital', 'name', 'phone', 'specialty', 'image', 'title', 'experience', 'rating', 'email', 'hours', 'linkedin_link')