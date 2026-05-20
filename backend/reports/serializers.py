from rest_framework import serializers
from backend.reports.models import Report


class ReportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = "__all__"
