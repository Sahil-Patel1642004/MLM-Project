from django.urls import path

from backend.attendance.views import AttendanceViewSet


# Simple explicit endpoints to avoid DRF router suffix/converter side effects during checks
urlpatterns = [
    path('', AttendanceViewSet.as_view({'get': 'list', 'post': 'create'}), name='attendance-list-create'),
]
