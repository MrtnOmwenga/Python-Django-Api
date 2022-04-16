from django.shortcuts import render
from django.http import HttpResponse

from .models import Employees

#Get employee using id
def Employees_by_id(request, id):
    employees = Employees.objects.get(pk = id)
    return HttpResponse(f"employee: {employees.name}")

#get employee from each department
def Employees_by_department(request, id):
    employees = Employees.objects.get(pk = id)
    return HttpResponse(f"employee: {employees.name}")

#get department using employee id
def Department_by_id(request, id):
    department = Employees.objects.get(pk = id)
    return HttpResponse(f"department: {department.department}")

#get employee position using employee id
def Position_by_id(request, id):
    position = Employees.objects.get(pk = id)
    return HttpResponse(f"position: {position.postiion}")

#get employee address using employee id
def Address_by_id(request, id):
    address = Employees.objects.get(pk = id)
    return HttpResponse(f"address: {address.address}")

#get employee id usijng employee name
def id_by_name(request, name):
    id = Employees.objects.get(pk = name)
    return HttpResponse(f"id: {id.id}")