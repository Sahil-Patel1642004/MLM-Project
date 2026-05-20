from rest_framework.routers import SimpleRouter
from backend.performance.views import *
router = SimpleRouter()

router.register(r'',PerformanceViewSet,basename='performance')

urlpatterns = router.urls   