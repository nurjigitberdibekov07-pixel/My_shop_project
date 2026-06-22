from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from urllib.parse import urlencode
from django.db.models import Q

from my_shop.models import Products
from my_shop.forms import ProductsForm, SearchForm


# Create your views here.

class ProductsListView(ListView):
    template_name = 'my_shop_forms/products/products.html'
    model = Products
    context_object_name = 'products'
    queryset = Products.objects.all().order_by('name')
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
            queryset = self.queryset.filter(Q(Q(name__icontains=self.search_value) | Q(stock__gt=0))).order_by('name')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProductDetailView(DetailView):
    template_name = 'my_shop_forms/products/detail_product.html'
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Products, pk=self.kwargs['pk'])
        return context


class ProductsCreateView(CreateView):
    template_name = 'my_shop_forms/products/product_add.html'
    form_class = ProductsForm

    def get_success_url(self):
        return reverse("product_detail", kwargs={'pk': self.object.pk})


class ProductsDeleteView(DeleteView):
    model = Products
    context_object_name = 'product'
    success_url = reverse_lazy("products")


class ProductsUpdateView(UpdateView):
    model = Products
    context_object_name = 'product'
    form_class = ProductsForm
    template_name = 'my_shop_forms/products/product_edit.html'

    def get_success_url(self):
        return reverse("product_detail", kwargs={'pk': self.object.pk})

