from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
class ManufacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacter
        fields = '__all__'
class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
class CartsElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartsElement
        fields = '__all__'