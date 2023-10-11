from rest_framework import serializers
from .models import Category,staticFeature

class CategorySerializer(serializers.ModelSerializer):
    # A serializer for Category model with child category support.

    child_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_child_categories(self, obj):
        # Retrieve and serialize child categories if they exist.

        # Get child categories related to the current Category object.
        child_categories = obj.child_categories.all()

        # If child categories exist, serialize them using this serializer.
        if child_categories:
            return CategorySerializer(child_categories, many=True).data
        else:
            return None

class FieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = staticFeature
        fields = '__all__'

