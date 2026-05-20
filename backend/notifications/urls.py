from rest_framework.routers import SimpleRouter
from backend.notifications.views import *
router = SimpleRouter()

router.register(r'',NotificationsViewSet,basename='notification')

urlpatterns = router.urls   