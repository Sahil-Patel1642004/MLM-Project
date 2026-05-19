from django.shortcuts import render
from .models import Hierarchy
from .serializers import HierarchySerializer
# Create your views here.

class EmployeeViewSet():
    qeryset = Hierarchy.objects.all()
    serializer_class = HierarchySerializer