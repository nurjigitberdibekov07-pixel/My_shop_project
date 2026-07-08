from django.shortcuts import render, redirect, get_object_or_404

from my_shop.models import Products, Categories


# Create your views here.


def categories_view(request):
    categories = Categories.objects.all()
    context = {'categories': categories}
    return render(request, "my_shop_forms/categories/categories.html", context)


def add_category(request):
    if request.method == "GET":
        return render(request, "my_shop_forms/categories/category_add.html")
    elif request.method == "POST":
        name = request.POST.get("name", "").strip()
        if not name:
            return render(request, "my_shop_forms/categories/category_add.html", {"error": "Please enter a name"})
        if Categories.objects.filter(name=name).exists():
            return render(request, "my_shop_forms/categories/category_add.html", {"error": "Category with this name already exists"})
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
        return render(request, "my_shop_forms/categories/category_edit.html", context)
    elif request.method == "POST":
        name = request.POST.get("name", "").strip()
        if not name:
            return render(request, "my_shop_forms/categories/category_edit.html", {"error": "Please enter a name"} )
        description = request.POST.get("description", "").strip()
        category.name = name
        category.description = description
        category.save()
        return redirect("categories_view")