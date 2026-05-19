from rest_framework import serializers
from .models import Company

class Companyserializers(serializers.ModelSerializer):
    class Meta:
        models = Company
        fields = "__all__"