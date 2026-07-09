from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, View

from my_shop.forms import OrderForm
from my_shop.models import Products, Cart


class AddToCartView(View):

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Products, pk = self.kwargs['pk'])
        cart_items = Cart.objects.filter(product=product).first()
        count = int(request.POST.get('count', 1))

        if cart_items:
            new_count = cart_items.count + count
            if new_count <= product.stock:
                cart_items.count = new_count
                cart_items.save()
            else:
                cart_items.count = product.stock
                cart_items.save()
        else:
            if product.stock >= count:
                Cart.objects.create(product=product, count=count)

        next_url = request.POST.get('next') or request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('products')


class CartListView(ListView):
    template_name = 'my_shop_forms/cart/cart.html'
    model = Cart
    context_object_name = 'products'
    queryset = Cart.objects.all().order_by('-count')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for i in self.get_queryset():
            total += i.count * i.product.price
        context['total'] = total
        context['form'] = OrderForm()
        return context

class CartDeleteView(DeleteView):
    model = Cart

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.count > 1:
            self.object.count -= 1
            self.object.save()
        else:
            self.object.delete()
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('cart')
        return next_url