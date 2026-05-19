from rest_framework import serializers
from .models import User

class Registerserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fname','lname', 'username', 'email', 'phone', 'password', 'referalcode', 'gender']
        extra_kwargs = {
            "password":{"write_only":True}
        }
class Loginserializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class Profileserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"