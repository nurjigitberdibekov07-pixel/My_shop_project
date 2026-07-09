from django.forms import ModelForm

from my_shop.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'phone_number']