from rest_framework import serializers  # type: ignore
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    role = serializers.IntegerField()
    city = serializers.CharField(max_length=10)