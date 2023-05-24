from django.urls import path
from . import views

urlpatterns = [
 path('products/', views.ProductList.as_view()),
 path('products/<int:pk>/', views.ProductDetail.as_view()),
 path('menuitems/', views.MenuItemList.as_view()),
 path('menuitems/<int:pk>/', views.MenuItemDetail.as_view()),
 path('orders/', views.OrderList.as_view()),
 path('orders/<int:pk>/', views.OrderDetail.as_view()),
]