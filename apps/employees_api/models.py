from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from apps.employees_api.choices import Choices
from apps.company_api.models import Company

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    country = CountryField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True, unique=True)
    about = models.TextField()
    designation = models.CharField(max_length=50)
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')  

    def __str__(self):
        return f"{self.name} - {self.phone}"
