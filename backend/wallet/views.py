from django.shortcuts import render
from backend.wallet.models import Wallet
from backend.wallet.serializers import WalletSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer