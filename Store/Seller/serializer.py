from rest_framework import serializers
from .models import Category,staticFeature

class CategorySerializer(serializers.ModelSerializer):
    # A serializer for Category model with child category support.

    childCategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id','categoryName','childCategories']

    def get_childCategories(self, obj):
        # Retrieve and serialize child categories if they exist.

        # Get child categories related to the current Category object.
        childCategories = obj.childCategories.all()

        # If child categories exist, serialize them using this serializer.
        if childCategories:
            return CategorySerializer(childCategories, many=True).data
        else:
            return None

class FieldsSerializer(serializers.ModelSerializer):
    describerFeatures = serializers.SerializerMethodField()

    class Meta:
        model = staticFeature
        fields = ['id', 'featureName', 'describerFeatures']

    def get_describerFeatures(self, obj):
       
        describerFeatures = obj.staticfeature_set.all()

        if describerFeatures:
            return FieldsSerializer(describerFeatures, many=True).data
        else:
            return None

