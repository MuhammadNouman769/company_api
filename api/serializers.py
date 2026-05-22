from rest_framework import serializers  # type: ignore
from .models import Student

class StudentSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    role = serializers.IntegerField()
    city = serializers.CharField(max_length=10)
    
    
    def create (self, validated_data):
        return Student.objects.create(**validated_data)