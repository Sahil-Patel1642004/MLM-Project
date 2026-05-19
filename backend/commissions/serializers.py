from rest_framework import serializers
from .models import Commissions


class Employehierachyserializers(serializers.ModelSerializer):
    class Meta:
        models = Commissions
        fields = "__all__"