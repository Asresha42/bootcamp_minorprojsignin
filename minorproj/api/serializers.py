from rest_framework import serializers
from .models import UsersAPI

class UserApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField()
    password = serializers.CharField()



