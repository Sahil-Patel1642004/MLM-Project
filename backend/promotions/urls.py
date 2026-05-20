from rest_framework.routers import SimpleRouter
from backend.promotions.views import *
router = SimpleRouter()

router.register(r'',PromotionsViewSet,basename='promotions')

urlpatterns = router.urls