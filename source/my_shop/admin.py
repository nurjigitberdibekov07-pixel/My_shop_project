from django.contrib import admin

# Register your models here.
from my_shop.models import Products, Categories, Cart, Order, IntermediateTable

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price", "image", "category", "created", "stock"]
    search_fields = ["name", "id"]
    fields = ["name", "description", "price", "image", "category", "created", "stock"]
    readonly_fields = ["created"]


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id","name", "description"]
    search_fields = ["name"]


class CartsAdmin(admin.ModelAdmin):
    list_display = ["id","product", "count"]
    fields = ["product", "count"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","name", "phone_number", "address", "created_at"]
    search_fields = ["name", "id"]


class IntermediateTableAdmin(admin.ModelAdmin):
    list_display = ["id","product", "order", "count"]

admin.site.register(Products, ProductAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Cart, CartsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(IntermediateTable, IntermediateTableAdmin)