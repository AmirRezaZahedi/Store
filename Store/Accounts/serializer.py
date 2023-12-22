from rest_framework import serializers
from .models import User,Seller,Customer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

    def save(self, **kwargs):

        self.instance = User.objects.create(**self.validated_data)
        return self.instance.id
