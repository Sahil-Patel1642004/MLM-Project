from django.shortcuts import render
from backend.hierarchy.models import Hierarchy
from backend.hierarchy.serializers import Employehierachyserializers
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class EmployehierachyViewSet(ModelViewSet):
    qeryset = Hierarchy.objects.all()
    serializer_class = Employehierachyserializers