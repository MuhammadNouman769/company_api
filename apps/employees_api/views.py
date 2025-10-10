from django.shortcuts import render
from rest_framework import viewsets
from apps.employees_api.models import Employee
from apps.employees_api.serializers import EmployeeSerializer
# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer
     