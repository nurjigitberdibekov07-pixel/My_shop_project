from django.urls import path
from my_shop.views import (ProductsListView,add_category, ProductsCreateView, ProductDetailView, categories_view, delete_category,
                           edit_category, ProductsDeleteView, ProductsUpdateView, AddToCartView, CartListView, CartDeleteView)
                           OrderCreateView)

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products'),
    path('categories/add/', add_category, name='add_category'),
    path('products/add/', ProductsCreateView.as_view(), name='add_product'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:pk>/delete/', delete_category, name='delete_category'),
    path('categories/<int:pk>/edit/', edit_category, name='edit_category'),
    path('products/<int:pk>/delete/', ProductsDeleteView.as_view(), name='delete_product'),
    path('products/<int:pk>/edit/', ProductsUpdateView.as_view(), name='edit_product'),
    path('product/<int:pk>/add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('cart/<int:pk>/delete/>', CartDeleteView.as_view(), name='delete_cart'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
]