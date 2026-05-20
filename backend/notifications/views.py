from rest_framework.viewsets import ModelViewSet
from backend.notifications.models import Notification
from backend.notifications.serializers import NotificationSerializer


class NotificationsViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
