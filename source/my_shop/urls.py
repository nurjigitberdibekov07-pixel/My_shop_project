from django.urls import path
from my_shop.views import (ProductsListView,add_category, add_product, product_detail, categories_view, delete_category,
                           edit_category, delete_product, edit_product)

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products'),
    path('categories/add/', add_category, name='add_category'),
    path('products/add/', add_product, name='add_product'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:pk>/delete/', delete_category, name='delete_category'),
    path('categories/<int:pk>/edit/', edit_category, name='edit_category'),
    path('products/<int:pk>/delete/', delete_product, name='delete_product'),
    path('products/<int:pk>/edit/', edit_product, name='edit_product'),
]