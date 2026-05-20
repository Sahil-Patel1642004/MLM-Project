from rest_framework.routers import SimpleRouter
from backend.salary.views import *
router = SimpleRouter()

router.register(r'',SalaryReportsViewSet,basename='salary')

urlpatterns = router.urls