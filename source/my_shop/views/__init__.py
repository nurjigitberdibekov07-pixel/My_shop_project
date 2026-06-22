from my_shop.views.products import ProductsListView, ProductDetailView, ProductsCreateView, ProductsDeleteView, ProductsUpdateView
from my_shop.views.categories import categories_view, add_category, delete_category, edit_category

__all__ = [
    'ProductsListView',
    'ProductDetailView',
    'ProductsCreateView',
    'ProductsDeleteView',
    'ProductsUpdateView'
    ]