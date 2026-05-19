from rest_framework import serializers
from .models import Salary

class SalaryIncrementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary
        fields = "__all__"