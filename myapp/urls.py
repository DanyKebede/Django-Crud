from django.urls import path, include
from rest_framework import routers
from .views import HospitalViewSet, DoctorViewSet

router = routers.DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]