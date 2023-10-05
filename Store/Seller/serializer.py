from rest_framework import serializers
from .models import Category,staticFeature

class CategorySerializer(serializers.Serializer):

    class Meta:
        model = Category
        fields = '__all__'

class FieldsSerializer(serializers.Serializer):

    class Meta:
        model = staticFeature
        fields = '__all__'

