from rest_framework import viewsets
from .models import Hospital, Doctor
from .serializers import HospitalSerializer, DoctorSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer