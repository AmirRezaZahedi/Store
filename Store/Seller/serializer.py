from rest_framework import serializers
from .models import Category,staticFeature,Product,intDynamicFeature,charDynamicFeature,ImageDynamicFeature
from customer.models import Order
from customer.serializer import CustomerSerializer

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

class IntDynamicSerializer(serializers.ModelSerializer):

    baseFeature = serializers.SerializerMethodField()
    class Meta:
        model = intDynamicFeature
        fields = ['featureNumber', 'baseFeature']

    def get_baseFeature(self, obj):
        basefeature = obj.baseFeature

        if basefeature:
            return FieldsSerializer(basefeature).data
        else:
            return None
class CharDynamicSerializer(serializers.ModelSerializer):

    baseFeature = serializers.SerializerMethodField()

    class Meta:
        model = charDynamicFeature
        fields = ['featureName', 'baseFeature']
    
    def get_baseFeature(self, obj):
        basefeature = obj.baseFeature

        if basefeature:
            return FieldsSerializer(basefeature).data
        else:
            return None


class ImageDynamicSerializer(serializers.ModelSerializer):

    baseFeature = serializers.SerializerMethodField()
    class Meta:
        model = ImageDynamicFeature
        fields = ['featureImage', 'baseFeature']

    def get_baseFeature(self, obj):
        basefeature = obj.baseFeature

        if basefeature:
            return FieldsSerializer(basefeature).data
        else:
            return None

class ProductSerializer(serializers.ModelSerializer):
    intdynamic = serializers.SerializerMethodField()
    chardynamic = serializers.SerializerMethodField()
    imagedynamic = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'product_quantity', 'intdynamic', 'chardynamic', 'imagedynamic']

    
    def get_intdynamic(self, obj):
        intdynamic = obj.intD.all()

        if intdynamic:
            return IntDynamicSerializer(intdynamic, many=True).data
        else:
            return None

    def get_chardynamic(self, obj):
        chardynamic = obj.charD.all()

        if chardynamic:
            return CharDynamicSerializer(chardynamic, many=True).data
        else:
            return None
    
    def get_imagedynamic(self, obj):
        imagedynamic = obj.imgD.all()

        if imagedynamic:
            return ImageDynamicSerializer(imagedynamic, many=True).data
        else:
            return None

class OrdersSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['address', 'quantity', 'product' ,'customer']

    def get_product(self, obj):
        product = obj.product

        if product:
            return ProductSerializer(product, many=True).data
        else:
            return None

    def get_customer(self, obj):
        customer = obj.customer

        if customer:
            return CustomerSerializer(customer, many=True).data
        else:
            return None
