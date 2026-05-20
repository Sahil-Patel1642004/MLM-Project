from rest_framework import serializers
from backend.salary.models import Salary

class SalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary
        fields = "__all__"