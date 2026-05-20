from rest_framework.viewsets import ModelViewSet

from backend.companies.models import Companies
from backend.companies.serializers import Companyserializers


class CompaniesViewSet(ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = Companyserializers

