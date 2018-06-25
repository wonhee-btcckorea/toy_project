from application.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RedisUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedisUser
        fields = '__all__'