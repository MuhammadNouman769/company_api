from django.contrib import admin
from django.urls import path, include
from apps.employees_api.views import EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
urlpatterns = [
     path('',include(router.urls))
    
]
