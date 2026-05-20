from rest_framework import serializers
from backend.employees.models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Employees
        fields = "__all__"
class Createserializer(serializers.ModelSerializer):
    class Meta:
        models = Employees
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
        model = Employees
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