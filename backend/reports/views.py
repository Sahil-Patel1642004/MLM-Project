from rest_framework.viewsets import ModelViewSet
from backend.reports.models import Report
from backend.reports.serializers import ReportsSerializer


class ReportsViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportsSerializer
