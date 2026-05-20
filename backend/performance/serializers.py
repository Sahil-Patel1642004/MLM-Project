from rest_framework import serializers
from backend.performance.models import Performance


class PerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performance
        fields = "__all__"