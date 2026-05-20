from rest_framework.viewsets import ModelViewSet
from backend.promotions.models import Promotion
from backend.promotions.serializers import PromotionSerializer


class PromotionsViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
