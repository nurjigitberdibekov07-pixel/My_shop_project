from django.forms import ModelForm
from my_shop.models import Categories

class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ["name", "description"]