from django.shortcuts import redirect
from django.views.generic import View

from my_shop.forms import OrderForm
from my_shop.models import IntermediateTable
from my_shop.views import cart


class OrderCreateView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            cart_items = cart.Cart.objects.all()
            for item in cart_items:
                IntermediateTable.objects.create(
                    order=order,
                    product=item.product,
                    count=item.count
                )
            cart_items.delete()
            return redirect('products')

        next_url = request.POST.get('next') or request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('products')
