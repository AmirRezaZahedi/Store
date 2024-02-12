
from rest_framework import serializers
from .models import User, Customer, Seller
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer ,UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name','access']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email','first_name','last_name']



class CreateCustomerSerializer(serializers.ModelSerializer):
    user=UserCreateSerializer()

    class Meta:
        model = Customer
        fields = ['id','user','store_name','store_type']

    def save(self, **kwargs):
        
        user_data = self.validated_data.pop('user')
        user_data['access']=1

        user_serializer = UserCreateSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user=user_serializer.save()

        self.instance = Customer.objects.create(**self.validated_data,user=user)


class CustomerSerializer(serializers.ModelSerializer):
    user=UserSerializer()

    class Meta:
        model = Customer
        fields = ['id','user','store_name','store_type']

    def save(self, **kwargs):
        
        if self.instance is not None:
            user_data = self.validated_data.pop('user')

            user_serializer = UserSerializer(self.instance.user,data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user=user_serializer.save()
            self.instance = self.update(self.instance, self.validated_data)

 
            



class CreateSellerSerializer(serializers.ModelSerializer):
    user=UserCreateSerializer()

    class Meta:
        model = Seller
        fields = ['id','user','store_name','store_type']

    def save(self, **kwargs):
        
        user_data = self.validated_data.pop('user')
        user_data['access']=0

        user_serializer = UserCreateSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user=user_serializer.save()

        self.instance = Seller.objects.create(**self.validated_data,user=user)


class SellerSerializer(serializers.ModelSerializer):
    user=UserSerializer()

    class Meta:
        model = Seller
        fields = ['id','user','store_name','store_type']

    def save(self, **kwargs):
        
        if self.instance is not None:
            user_data = self.validated_data.pop('user')

            user_serializer = UserSerializer(self.instance.user,data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user=user_serializer.save()
            self.instance = self.update(self.instance, self.validated_data)
