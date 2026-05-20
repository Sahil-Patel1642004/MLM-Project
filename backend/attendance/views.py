from rest_framework.viewsets import ModelViewSet

from backend.attendance.models import Attendance
from backend.attendance.serializers import AttendanceSerializer


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

