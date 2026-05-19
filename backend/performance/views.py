from django.shortcuts import render
from .models import Performance
from .serializers import PerformanceSerializer
# Create your views here.

class PerformanceViewSet():
    qeryset = Performance.objects.all()
    serializer_class = PerformanceSerializer