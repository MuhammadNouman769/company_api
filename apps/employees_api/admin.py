# apps/employees_api/admin.py
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'company', 'email', 'phone')
    list_filter = ('designation', 'company')
    search_fields = ('name', 'email', 'company__name')
