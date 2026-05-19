from django.shortcuts import render
from .models import Reports
from .serializers import ReportsSerializer
# Create your views here.

class ReportsViewSet():
    qeryset = Reports.objects.all()
    serializer_class = ReportsSerializer