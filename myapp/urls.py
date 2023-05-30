from django.urls import path, include
from rest_framework import routers
from .views import HospitalViewSet, DoctorViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token, name='api-token-auth'),
]
