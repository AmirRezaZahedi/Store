from rest_framework import serializers
from .models import Customer
from Accounts.serializers import UserCreateSerializer


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