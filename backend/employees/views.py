from django.shortcuts import render
from .models import Employees
from .serializers import EmployeesSerializer
# Create your views here.

class EmployeeViewSet():
    qeryset = Employees.objects.all()
    serializer_class = EmployeesSerializer