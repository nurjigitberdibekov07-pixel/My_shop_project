from my_shop.views.products import ProductsListView, ProductDetailView, ProductsCreateView, ProductsDeleteView, ProductsUpdateView
from my_shop.views.categories import categories_view, add_category, delete_category, edit_category
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
    ]