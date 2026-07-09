from my_shop.views.products import ProductsListView, ProductDetailView, ProductsCreateView, ProductsDeleteView, ProductsUpdateView
from my_shop.views.categories import CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView
from my_shop.views.cart import AddToCartView, CartListView, CartDeleteView
from my_shop.views.order import OrderCreateView

__all__ = [
    'ProductsListView',
    'ProductDetailView',
    'ProductsCreateView',
    'ProductsDeleteView',
    'ProductsUpdateView',
    'AddToCartView',
    'CartListView',
    'CartDeleteView',
    'OrderCreateView',
    'CategoryListView',
    'CategoryCreateView',
    'CategoryDeleteView',
    'CategoryUpdateView',
    ]