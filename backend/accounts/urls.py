from django.urls import path

from backend.accounts.views import AccountsViewSet


urlpatterns = [
    path('', AccountsViewSet.as_view({'get': 'list', 'post': 'create'}), name='accounts-list-create'),
]

