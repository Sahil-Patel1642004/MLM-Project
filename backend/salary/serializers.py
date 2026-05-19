from rest_framework import serializers
from .models import SalaryIncrement


class SalaryIncrementSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalaryIncrement
        fields = "__all__"