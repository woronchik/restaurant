from rest_framework import serializers
from .models import Product, MenuItem, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'is_available', 'preparation_time')


class MenuItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = MenuItem
        fields = ('id', 'product', 'special_instructions')


class OrderSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'menu_items', 'total_price', 'delivery_address', 'payment_method', 'delivery_time', 'customer_name', 'customer_phone', 'customer_email')