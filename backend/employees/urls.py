from django.urls import path

from backend.employees.views import EmployeeViewSet

urlpatterns = [
    path('', EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employees-list-create'),
]

