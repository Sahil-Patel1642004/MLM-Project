from django.shortcuts import render
from .models import accounts
from .serializers import AccountsSerializer
# Create your views here.


class AccountsViewSet():
    
    queryset = accounts.objects.all()
    serializer_class = AccountsSerializer