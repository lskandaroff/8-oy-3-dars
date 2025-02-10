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

    path('comments', CommentListView.as_view()),
    path('comment/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('comment/create', CommentListView.as_view()),
    path('comment/delete/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('comment/update/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view()),

    path('Themes', ThemeListView.as_view()),
    path('theme/<int:pk>', ThemeRetrieveUpdateDestroyAPIView.as_view()),
    path('theme/create', ThemeListView.as_view()),
    path('theme/delete/<int:pk>', ThemeRetrieveUpdateDestroyAPIView.as_view()),
    path('theme/update/<int:pk>', ThemeRetrieveUpdateDestroyAPIView.as_view()),

    path('reply_comment', Reply_to_CommentListView.as_view()),
    path('reply_comment/<int:pk>', Reply_to_CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('reply_comment/create', Reply_to_CommentListView.as_view()),
    path('reply_comment/delete/<int:pk>', Reply_to_CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('reply_comment/update/<int:pk>', Reply_to_CommentRetrieveUpdateDestroyAPIView.as_view()),
]