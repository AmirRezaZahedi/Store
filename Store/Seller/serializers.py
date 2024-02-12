from rest_framework import serializers
from .models import Seller,Category,staticFeature,Product,intDynamicFeature,charDynamicFeature,ImageDynamicFeature
from customer.models import Order
from Accounts.serializers import CustomerSerializer


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


    class Meta:
        model = staticFeature
        fields = ['featureName']
    '''
    def get_describerFeatures(self, obj):
       
        describerFeatures = obj.describerFeatures.all()

        if describerFeatures:
            return FieldsSerializer(describerFeatures, many=True).data
        else:
            return None
    '''
        


class IntDynamicSerializer(serializers.ModelSerializer):

    baseFeature = FieldsSerializer()

    class Meta:
        model = intDynamicFeature
        fields = ['baseFeature', 'featureNumber']
        
    def save(self, products_id, **kwargs):
        
        baseFeature = self.validated_data.pop('baseFeature')
        baseFeature = staticFeature.objects.get(featureName=baseFeature["featureName"])
        self.instance = intDynamicFeature.objects.create( **self.validated_data,products_id=products_id,baseFeature=baseFeature)

class CharDynamicSerializer(serializers.ModelSerializer):

    baseFeature = FieldsSerializer()
    class Meta:
        model = charDynamicFeature
        fields = ['baseFeature', 'featureName']
        
    def save(self, products_id, **kwargs):
        
        baseFeature = self.validated_data.pop('baseFeature')
        baseFeature = staticFeature.objects.get(featureName=baseFeature["featureName"])
        self.instance = charDynamicFeature.objects.create( **self.validated_data,products_id=products_id,baseFeature=baseFeature)


class ImageDynamicSerializer(serializers.ModelSerializer):

    baseFeature = FieldsSerializer()

    class Meta:
        model = ImageDynamicFeature
        fields = ['featureImage', 'baseFeature']

    def save(self, products_id, **kwargs):
        
        baseFeature = self.validated_data.pop('baseFeature')
        baseFeature = staticFeature.objects.get(featureName=baseFeature["featureName"])
        self.instance = ImageDynamicFeature.objects.create( **self.validated_data,products_id=products_id,baseFeature=baseFeature)


class ProductSerializer(serializers.ModelSerializer):

    intD = IntDynamicSerializer(many=True)
    charD = CharDynamicSerializer(many=True)
    imgD = ImageDynamicSerializer(many=True)


    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'product_quantity', 'intD', 'charD', 'imgD','category']
        
    def save(self, **kwargs):
        print(self.validated_data)
        
        intD_data = self.validated_data.pop('intD')
        charD_data = self.validated_data.pop('charD')
        imgD_data = self.validated_data.pop('imgD')
        
        #seller = self.context['seller_id']
        self.instance = Product.objects.create(**self.validated_data,seller_id=1)
        
        product_id = self.instance.id
        
        int_serializer = IntDynamicSerializer(many=True,data=intD_data)
        if int_serializer.is_valid():
            int_serializer.save(products_id=product_id)


        char_serializer = CharDynamicSerializer(many=True,data=charD_data)
        if char_serializer.is_valid():
            char_serializer.save(products_id=product_id)


        img_serializer = ImageDynamicSerializer(many=True,data=imgD_data)
        if img_serializer.is_valid():
            img_serializer.save(products_id=product_id)


        '''
        for obj in intD_data:
            print(obj)
            int_serializer = IntDynamicSerializer(data=obj)
            if int_serializer.is_valid():
                int_serializer.save(products_id=product_id)
        
        for obj in charD_data:
            char_serializer = CharDynamicSerializer(data=obj)
            if char_serializer.is_valid():
                char_serializer.save(products_id=product_id)
        
        for obj in imgD_data:
            img_serializer = ImageDynamicSerializer(data=obj)
            if img_serializer.is_valid():
                img_serializer.save(products_id=product_id)
        '''
                
        #self.quantity = self.validated_data['quantity']
        #self.name = self.validated_data['name']
        #self.name = self.validated_data['price']
        
        
        
   
class OrdersSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Order
        fields = ['address', 'quantity', 'product' ,'customer']
