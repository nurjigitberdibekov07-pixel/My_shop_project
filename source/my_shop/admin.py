from django.contrib import admin

# Register your models here.
from my_shop.models import Products, Categories

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price", "image", "category", "created", "stock"]
    search_fields = ["name", "id"]
    fields = ["name", "description", "price", "image", "category", "created", "stock"]
    readonly_fields = ["created"]


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id","name", "description"]
    search_fields = ["name"]

admin.site.register(Products, ProductAdmin)
admin.site.register(Categories, CategoriesAdmin)