from rest_framework.viewsets import ModelViewSet

from backend.employees.models import Employees
from backend.employees.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

