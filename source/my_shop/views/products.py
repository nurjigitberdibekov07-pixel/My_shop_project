from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from urllib.parse import urlencode

from my_shop.models import Products
from my_shop.forms import ProductsForm, SearchForm


# Create your views here.
# def products_view(request):
#     products = Products.objects.filter(stock__gt=0).order_by("category__name", "name")
#     search_form = SearchForm(request.GET)
#
#     if search_form.is_valid():
#         name = search_form.cleaned_data.get('name')
#         if name:
#             products = products.filter(name__icontains=name)
#
#     context = {'products': products, 'search_form': search_form}
#     return render(request, "my_shop_forms/products.html", context)

class ProductsListView(ListView):
    template_name = 'my_shop_forms/products/products.html'
    model = Products
    context_object_name = 'products'
    queryset = Products.objects.all()
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET )

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']


    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_value:
            queryset = self.queryset.filter(name__icontains=self.search_value)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context

def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {'product': product}
    return render(request, "my_shop_forms/detail_product.html", context)

def add_product(request):
    form = ProductsForm()
    if request.method == "GET":
        return render(request, "my_shop_forms/product_add.html", {'form': form})

    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
        else:
            return render(request, "my_shop_forms/product_add.html", {'form': form})

def delete_product(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Products, pk=pk)
        product.delete()
    return redirect("products")


def edit_product(request, pk):
    product = Products.objects.get(pk=pk)
    form = ProductsForm(instance=product)
    context = {'product': product, 'form': form}
    if request.method == "GET":
        return render(request, "my_shop_forms/product_edit.html", context)

    if request.method == "POST":
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
        return render(request, "my_shop_forms/product_edit.html", context)