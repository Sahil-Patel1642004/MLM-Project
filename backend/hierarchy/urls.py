from rest_framework.routers import SimpleRouter
from backend.hierarchy.views import *
router = SimpleRouter()

router.register(r'',EmployehierachyViewSet,basename='Employehierachy')

urlpatterns = router.urls