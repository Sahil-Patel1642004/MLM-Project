from django.shortcuts import render
from backend.salary.models import Salary
from backend.salary.serializers import SalarySerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class SalaryReportsViewSet(ModelViewSet):
    qeryset = Salary.objects.all()
    serializer_class = SalarySerializer