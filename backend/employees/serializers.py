from rest_framework import serializers
from .models import Employe

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Employe
        fields = "__all__"
class Createserializer(serializers.ModelSerializer):
    class Meta:
        models = Employe
        fields = [
            "employee_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "company",
            "role",
            "manager",
            "sponsor",
            "salary",
            "joining_date",
        ]
class Listserializers(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = [
            "employee_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "company",
            "role",
            "salary",
        ]