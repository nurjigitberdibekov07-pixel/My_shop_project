from django.shortcuts import render, redirect, get_object_or_404

from my_shop.models import Products, Categories
from my_shop.forms import ProductsForm, CategoriesForm

# Create your views here.
def products_view(request):
    products = Products.objects.filter(stock__gt=0).order_by("category__name", "name")
    context = {'products': products}
    return render(request, "my_shop_forms/products.html", context)

def categories_view(request):
    categories = Categories.objects.all()
    context = {'categories': categories}
    return render(request, "my_shop_forms/categories.html", context)

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


def add_category(request):
    if request.method == "GET":
        return render(request, "my_shop_forms/category_add.html")
    elif request.method == "POST":
        name = request.POST.get("name", "").strip()
        if not name:
            return render(request, "my_shop_forms/category_add.html", {"error": "Please enter a name"})
        if Categories.objects.filter(name=name).exists():
            return render(request, "my_shop_forms/category_add.html", {"error": "Category with this name already exists"})
        Categories.objects.create(name=name, description=request.POST.get("description", "").strip())
    return redirect("categories_view")

def delete_category(request, pk):
    category = Categories.objects.get(pk=pk)
    Products.objects.filter(category=category).delete()
    category.delete()
    return redirect("categories_view")

def edit_category(request, pk):
    category = Categories.objects.get(pk=pk)
    if request.method == "GET":
        context = {'category': category}
        return render(request, "my_shop_forms/category_edit.html", context)
    elif request.method == "POST":
        name = request.POST.get("name", "").strip()
        if not name:
            return render(request, "my_shop_forms/category_edit.html", {"error": "Please enter a name"} )
        description = request.POST.get("description", "").strip()
        category.name = name
        category.description = description
        category.save()
        return redirect("categories_view")