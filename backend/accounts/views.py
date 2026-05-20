from rest_framework.viewsets import ModelViewSet

from backend.accounts.models import Accounts
from .serializers import Registerserializers


class AccountsViewSet(ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = Registerserializers

