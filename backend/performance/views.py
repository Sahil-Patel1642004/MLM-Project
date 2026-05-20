from django.shortcuts import render
from backend.performance.models import Performance
from backend.performance.serializers import PerformanceSerializer
# Create your views here.
from rest_framework.viewsets import ModelViewSet


class PerformanceViewSet(ModelViewSet):
    qeryset = Performance.objects.all()
    serializer_class = PerformanceSerializer