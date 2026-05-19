from django.shortcuts import render
from .models import Wallet
from .serializers import WalletSerializer
# Create your views here.

class WalletViewSet():
    qeryset = Wallet.objects.all()
    serializer_class = WalletSerializer