from apps.employees_api.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
     id = serializers.ReadOnlyField()
     class Meta:
          model = Employee
          fields = '__all__'
          