from rest_framework import serializers
from .models import User, Customer, Seller
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from django.contrib.auth.hashers import make_password

class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

    def save(self, **kwargs):
        self.validated_data["password"] = make_password(self.validated_data['password'])
        self.instance = User.objects.create(**self.validated_data)
        return self.instance.id


class CustomerSerializer(serializers.ModelSerializer):
    user=UserCreateSerializer()
    
    class Meta:
        model = Customer
        fields = ['user']

    def save(self, **kwargs):
        
        user_data = self.validated_data.pop('user')

        user_serializer = UserCreateSerializer(data=user_data)
        if user_serializer.is_valid():
            user_id=user_serializer.save()
        self.instance = Customer.objects.create(**self.validated_data,user_id=user_id)



class SellerSerializer(serializers.ModelSerializer):
    user=UserCreateSerializer()

    class Meta:
        model = Seller
        fields = ['user','store_name','store_type']

    def save(self, **kwargs):
        
        user_data = self.validated_data.pop('user')

        user_serializer = UserCreateSerializer(data=user_data)
        if user_serializer.is_valid():
            user_id=user_serializer.save()
        
        self.instance = Seller.objects.create(**self.validated_data,user_id=user_id)
