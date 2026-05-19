from django.shortcuts import render
from .models import attendence
from .serializers import AttendanceSerializer
# Create your views here.


class AccountsViewSet():
    
    queryset = attendence.objects.all()
    serializer_class = AttendanceSerializer