from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('menuitems/', views.MenuItemList.as_view()),
    path('orders/', views.OrderList.as_view()),
]
