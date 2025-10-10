from django.shortcuts import render
from rest_framework import viewsets
from apps.company_api.models import Company
from apps.company_api.serializers import CompanySerializer
from rest_framework.decorators import action
from apps.employees_api.models import Employee
from apps.employees_api.serializers import EmployeeSerializer
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
     queryset = Company.objects.all()
     serializer_class = CompanySerializer
     
     
     @action(detail=True,methods=['get'])
     def employees(self,request,pk=None):
          try:       
               company = Company.objects.get(pk=pk)
               employees = Employee.objects.filter(company=company)
               employees_serializer = EmployeeSerializer(employees,
               many=True, context={'request':request}) 
               return Response(employees_serializer.data)
          except Exception as e:
               print(e)
               return Response({
                    'message':'this copmany not exit' 
               })
               