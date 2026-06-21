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

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Profile
        fields = ['id', 'username', 'role', 'full_name', 'phone', 'address']
        read_only_fields = ['role']

from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = ['id', 'user', 'username', 'created_at', 'status', 'total_price', 'items']
        read_only_fields = ['user', 'total_price', 'status']