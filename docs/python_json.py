# '''   Python Json
# python json has a built in pakage called json, which is used to work with json data.

# type of methods we will read in json or python json
#   1. dump
#   2. loads

#   i.dumps(data)-- this is used to convert python object into json string.
#       example:-
#       To use json package First we have to import it.
#       import json
# '''
# import json

# from django.db import models
# python_data = {'name':'Nouman','age':25}
# json_data = json.dumps(python_data)
# print(json_data)
# print(type(json_data))


# '''loads(data) - this is used to parse json string and convert it into python object.
# example:-
# '''
# json_data = '{"name":"Nouman","age":25}'
# python_data = json.loads(json_data)
# print(python_data)
# print(type(python_data))             

# ''' 
# 1. Serialization
#    in Django Rest Framwork, serializers are responsible for conveting complex data
#    such as querysets or model instances to native Python datatypes ( called serialization )
#    that can then be easily rendered into JSON,xml or other content types which is understandable by frontend.
   
# 2. Deserialization
#    serializers also provide deserialization, allowing parsed data to be converted back into complex types,
#    after validating the incoming data.
#    This is particularly useful when handling incoming data from API requests,
#    ensuring that the data is valid
   
# 1. Serializers Class    
#    A serializer class is very similer to a django form and ModelForm class,
#    and includes similar validation behavior.
#    It defines the fields that should be included in the serialized output,
#    and can also include custom validation logic.  
   
#    DRF provides a serializer class which gives you a powerful,
#    flexible and customizable way to control the output of your API responses. 
   
#    how to create a serializer class?
#    To create a serializer class, you need to import the serializers module from rest_framework,
#    and then define a new class that inherits from serializers.Serializer or serializers.ModelSerializer.
#    You can then define the fields that you want to include in the serialized output,
   
# example:-
# UserModel
# '''
# from django.db import models
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     phone = models.CharField(max_length=15)
#     roll_number = models.CharField(max_length=10)
#     city = models.CharField(max_length=50, null=True, blank=True)  # Optional field   
# '''   
#    example User Serializer:-
# '''   

# from rest_framework import serializers

# class UserSerializer(serializers.Serializer):            
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     phone = serializers.CharField(max_length=15)
#     roll_number = serializers.CharField(max_length=10)
#     city = serializers.CharField(max_length=50, required=False)  # Optional field
    
# '''
#       ----------------------------------------------------------------
#       | id | name   | age | phone       | roll_number  | city        |
#       ----------------------------------------------------------------
#       | 1  | Nouman | 25  | 03028186762 | 101          | Karachi     |
#       ----------------------------------------------------------------
#       | 2  | Ali    | 30  | 0387654321  | 102          | Lahore      |
#       ----------------------------------------------------------------
#       | 3  | Ahmed  | 28  | 0355555555  | 103          | Islamabad   |
#       ----------------------------------------------------------------
#       | 4  | Sara   | 22  | 0444444444  | 104          | Multan      |
#       ----------------------------------------------------------------
#       | 5  | Ayesha  | 27  | 0333333333  | 105         | Faisalabad  |
#       ----------------------------------------------------------------
#       | 6  | Bilal  | 24  | 0322222222  | 106          | Peshawar    |
#       ----------------------------------------------------------------
#       | 7  | Fatima | 26  | 0311111111  | 107          | Quetta      |
#       ----------------------------------------------------------------


#  1.Serialization   
 
#  create quert set
#   user = User.objects.all()  # Assuming you have a User model
#   serializer = UserSerializer(user, many=True)
 
# 2. JsonRenderer
#    JsonRenderer is a class provided by Django Rest Framework that is responsible for rendering the serialized data
#    into JSON format. It takes the serialized data and converts it into a JSON string that can be sent as a response to API requests.
#    JsonRenderer is typically used in conjunction with serializers to produce JSON responses for API endpoints.
   
#    example:-
# '''   
# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView
# class UserListView(APIView):
#       def get(self, request):
#          users = User.objects.all()  # Assuming you have a User model
#          serializer = UserSerializer(users, many=True)
#          json_data = JSONRenderer().render(serializer.data)
#          return Response(json_data, content_type='application/json')  

# '''   
# 3. JsonResponse
#    i.JsonResponse is a subclass of Django's HttpResponse that is specifically designed for returning JSON data.
#      It takes a Python dictionary or list and automatically converts it into a JSON string,
#      setting the appropriate content type for the response.
#      JsonResponse is a convenient way to return JSON data from Django views without needing
#      to manually serialize the data or set the content type.
#   ii.JsonResponse is a subclass of HttpResponse, so it inherits all the methods and properties of HttpResponse,
#      but it also provides some additional functionality that is specific to working with JSON data. 
#  iii. The safe parameter in JsonResponse is used to indicate whether the data being passed to JsonResponse
#       is a dictionary or not.By default, safe is set to True, which means that the data must be a dictionary.
#       If you want to pass a list or any other non-dictionary data, you need to set
#       safe to False. This is a security measure to prevent accidental exposure of sensitive data,
#       as JSON responses are often used in APIs and can be consumed by external clients.     
#    example:-
# '''
# from django.http import JsonResponse
# from rest_framework.views import APIView
# class UserListView(APIView):
#     def get(self, request):
#         users = User.objects.all()  # Assuming you have a User model
#         serializer = UserSerializer(users, many=True)
#         return JsonResponse(serializer.data, safe=False)
 

