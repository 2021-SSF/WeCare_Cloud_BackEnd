"""wecare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from facility import views

urlpatterns = [
    path('', views.facility_room_list, name="facilityRoom_list"), # 병원 병실 리스트
    path('rooms/<int:room_id>/', views.facility_room_detail, name="facility_detail"),  # 방에 맞는 환자들 정보 가져오기
    path('rooms/<int:room_id>/elder/<int:elder_id>/', views.elder_detail, name="elder_detail"),  # 환자 상세정보
    path('occupancy/{data}/', views.elder_status_create, name="elderStatus_Create"),  # 환자 상세정보
]
