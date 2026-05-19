from rest_framework import serializers
from .models import Companies

class Companyserializers(serializers.ModelSerializer):
    class Meta:
        models = Companies
        fields = "__all__"