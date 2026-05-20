from rest_framework import serializers
from backend.hierarchy.models import Hierarchy


class Employehierachyserializers(serializers.ModelSerializer):
    class Meta:
        models = Hierarchy
        fields = "__all__"