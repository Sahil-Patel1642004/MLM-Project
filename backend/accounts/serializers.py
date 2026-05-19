from rest_framework import serializers
from .models import Accounts

class Registerserializers(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['id', 'fname','lname', 'username', 'email', 'phone', 'password', 'referalcode', 'gender']
        extra_kwargs = {
            "password":{"write_only":True}
        }
class Loginserializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class Profileserializers(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = "__all__"