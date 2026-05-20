from rest_framework.routers import SimpleRouter
from backend.wallet.views import WalletViewSet
router = SimpleRouter()

router.register(r'',WalletViewSet,basename='wallet')

urlpatterns = router.urls