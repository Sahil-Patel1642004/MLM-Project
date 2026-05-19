from django.shortcuts import render
from .models import Company
from .serializers import CompaniesSerializer
# Create your views here.


class CompaniesViewSet():

    qeryset = Company.objects.all()
    serializer_class = CompaniesSerializer
        