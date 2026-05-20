from rest_framework.routers import SimpleRouter
from backend.reports.views import *
router = SimpleRouter()

router.register(r'',ReportsViewSet,basename='report')

urlpatterns = router.urls