from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from my_shop.forms import CategoriesForm
from my_shop.models import Products, Categories
# Create your views here.

class CategoryListView(ListView):
    model = Categories
    template_name = 'my_shop_forms/categories/categories.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    form_class = CategoriesForm
    template_name = 'my_shop_forms/categories/category_add.html'
    context_object_name = 'categories'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('cart')
        return next_url

class CategoryDeleteView(DeleteView):
    model = Categories

    def get_success_url(self):
        return reverse("categories_view")

class CategoryUpdateView(UpdateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'my_shop_forms/categories/category_edit.html'
    context_object_name = 'category'

    def get_success_url(self):
        return reverse("categories_view")


