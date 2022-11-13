from rest_framework import serializers

from useraccount.models import CustomUser

from .models import Client

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['uuid', 'username']

class ClientSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['user']