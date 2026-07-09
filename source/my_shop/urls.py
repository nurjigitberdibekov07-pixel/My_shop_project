from django.urls import path
from my_shop.views import (ProductsListView,CategoryCreateView, ProductsCreateView, ProductDetailView, CategoryListView, CategoryDeleteView,
                           CategoryUpdateView, ProductsDeleteView, ProductsUpdateView, AddToCartView, CartListView, CartDeleteView,
                           OrderCreateView)

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products'),
    path('categories/add/', CategoryCreateView.as_view(), name='add_category'),
    path('products/add/', ProductsCreateView.as_view(), name='add_product'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/', CategoryListView.as_view(), name='categories_view'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete_category'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='edit_category'),
    path('products/<int:pk>/delete/', ProductsDeleteView.as_view(), name='delete_product'),
    path('products/<int:pk>/edit/', ProductsUpdateView.as_view(), name='edit_product'),
    path('product/<int:pk>/add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='delete_cart'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
]