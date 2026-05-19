from rest_framework import serializers
from .models import Employehierachy


class Employehierachyserializers(serializers.ModelSerializer):
    class Meta:
        models = Employehierachy
        fields = "__all__"