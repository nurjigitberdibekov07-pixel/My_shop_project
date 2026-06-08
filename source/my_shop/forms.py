from django.forms import ModelForm, widgets, IntegerField, DecimalField
from django.core.exceptions import ValidationError
from my_shop.models import Products, Categories

class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ["name", "description"]


class ProductsForm(ModelForm):
    stock = IntegerField(min_value=0, widget=widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Stock"}))
    price = DecimalField(max_digits=7, decimal_places=2, widget=widgets.NumberInput(attrs={"class": "form-control", "step": "0.01", "min": "1","placeholder": "Price"}))  # ← две закрывающие скобки
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'image', 'stock', 'category']

        widgets = {
            "description": widgets.Textarea(attrs={"class":"form-control" , "cols": "40", "rows": "5", "placeholder": "description"}),
            "name": widgets.TextInput(attrs={"class":"form-control" , "placeholder": "Name"}),
            "image": widgets.TextInput(attrs={"class":"form-control", "placeholder": "Image"}),
            "category": widgets.Select(attrs={"class": "form-select", "placeholder": "Category"}),
        }

        labels = {
            "name": "name",
            "description": "description",
            "price": "price",
            "image": "image",
            "stock": "stock",
            "category": "category",
        }

        error_messages = {
            "name": {
                "required": "Please enter product name",
            },
            "stock":{
                "required": "Please enter product stock",
                "min_value": "Please enter product stock minimum value",
            }
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if len(name) < 3:
            raise ValidationError("Name must be at least 3 characters long")
        if len(name) > 100:
            raise ValidationError("Name must be at most 100 characters long")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "").strip()
        if len(description) > 3000:
            raise ValidationError("Description must be at most 3000 characters long")
        return description

