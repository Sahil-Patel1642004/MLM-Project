from django.urls import path

from backend.commissions.views import CommissionsViewSet

urlpatterns = [
    path('', CommissionsViewSet.as_view({'get': 'list', 'post': 'create'}), name='commissions-list-create'),
]
