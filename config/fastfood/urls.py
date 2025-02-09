from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductListView.as_view()),
    path('product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('product/create', ProductListView.as_view()),
    path('product/delete/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('product/update/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),

    path('orders', OrderListView.as_view()),
    path('order/<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view()),
    path('order/create', OrderListView.as_view()),
    path('order/delete/<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view()),
    path('order/update/<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view()),

    path('customers', CustomerListView.as_view()),
    path('customer/<int:pk>', CustomerRetrieveUpdateDestroyAPIView.as_view()),
    path('customer/create', CustomerListView.as_view()),
    path('customer/delete/<int:pk>', CustomerRetrieveUpdateDestroyAPIView.as_view()),
    path('customer/update/<int:pk>', CustomerRetrieveUpdateDestroyAPIView.as_view()),
]