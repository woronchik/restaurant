from rest_framework import generics
from .models import Product, MenuItem, Order
from .serializers import ProductSerializer, MenuItemSerializer, OrderSerializer

class ProductList(generics.ListCreateAPIView):
 queryset = Product.objects.all()
 serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Product.objects.all()
 serializer_class = ProductSerializer

class MenuItemList(generics.ListCreateAPIView):
 queryset = MenuItem.objects.all()
 serializer_class = MenuItemSerializer

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = MenuItem.objects.all()
 serializer_class = MenuItemSerializer

class OrderList(generics.ListCreateAPIView):
 queryset = Order.objects.all()
 serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Order.objects.all()
 serializer_class = OrderSerializer
