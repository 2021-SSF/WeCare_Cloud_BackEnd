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
from django.urls import path

from facility import views

urlpatterns = [
    path('<str:facility_id>/', views.facilityRoom_list, name="facilityRoom_list"), #병원 정보 페이지 리스트
    path('<str:facility_id>/room/<int:room_id>/', views.facility_detail, name="facility_detail"),  # 병원정보 클릭하면 이동하는 페이지

    path('<str:facility_id>/elders/add/', views.elders_add, name="elders_add"),  # 환자 추가 모달창
    path('<str:facility_id>/diet/add/', views.diet_add, name="diet_add"),  # 식단 추가 모달창  (오늘 날짜가 없으면 수정)

    path('<str:facility_id>/elders/detail/<str:elders_id>/', views.elders_detail, name="elders_detail"),  # 환자 상세정보
    path('<str:facility_id>/elders/update/<str:elders_id>/', views.elders_update, name="elders_update"),  # 환자 정보 수정
    path('<str:facility_id>/elders/delete/<str:elders_id>/' , views.elders_delete, name="elders_delete"),  # 환자 정보 삭제

]