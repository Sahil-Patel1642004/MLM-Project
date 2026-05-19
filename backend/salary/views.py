from django.shortcuts import render
from .models import Salary
from .serializers import SalarySerializer
# Create your views here.

class ReportsViewSet():
    qeryset = Salary.objects.all()
    serializer_class = SalarySerializer