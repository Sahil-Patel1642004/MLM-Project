from rest_framework import serializers
from backend.commissions.models import Commissions


class CommissionsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Commissions
        fields = "__all__"