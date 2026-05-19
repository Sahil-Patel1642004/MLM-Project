from django.shortcuts import render
from .models import Notifications
from .serializers import NotificationsSerializer
# Create your views here.

class NotificationsViewSet():
    qeryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer