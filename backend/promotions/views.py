from django.shortcuts import render
from .models import Promotions
from .serializers import PromotionsSerializer
# Create your views here.

class PromotionsViewSet():
    qeryset = Promotions.objects.all()
    serializer_class = PromotionsSerializer