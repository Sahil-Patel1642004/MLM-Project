from rest_framework.routers import SimpleRouter
from backend.companies.views import *

router = SimpleRouter()

router.register(r'',CompaniesViewSet,basename='company')

urlpatterns = router.urls