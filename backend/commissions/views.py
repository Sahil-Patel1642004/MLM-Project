from django.shortcuts import render
from .models import commissions
from .serializers import commissionsSerializer
# Create your views here.


class CommissionsViewSet():
    
    queryset = commissions.objects.all()
    serializer_class = CommissionsSerializer