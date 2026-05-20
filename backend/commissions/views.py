from rest_framework.viewsets import ModelViewSet

from backend.commissions.models import Commissions
from backend.commissions.serializers import CommissionsSerializer


class CommissionsViewSet(ModelViewSet):
    queryset = Commissions.objects.all()
    serializer_class = CommissionsSerializer
