from django.forms import ModelForm, widgets

from my_shop.models import Products, Categories

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'image', 'stock', 'category']

        widgets = {
            "description": widgets.Textarea(attrs={"cols": "40", "rows": "5"})
        }