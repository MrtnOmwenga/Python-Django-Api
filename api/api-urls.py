from django.urls import path

#import views
from . import views
#Create URLS
urlpatterns = [
    path('employee_by_id/<id>', views.Employees_by_id, name = 'Employee_by_id'),
    path('department_by_id/<id>', views.Department_by_id, name = 'Department_by_id'),
    path('position_by_id/<id>', views.Position_by_id, name = 'Position_by_id'),
    path('address_by_id/<id>', views.Address_by_id, name = 'Address_by_id'),
    path('id_by_name/<name>', views.id_by_name, name = 'Id_by_name')
    ]