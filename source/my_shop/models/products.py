from django.db import models
from django.urls import reverse

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Name")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")
    category = models.ForeignKey("my_shop.Categories", on_delete=models.RESTRICT, related_name="Products", null=False, blank=False,)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name='Price')
    image = models.CharField(max_length=300, null=False, blank=False, verbose_name='Image')
    stock = models.IntegerField(default=0, null=False, blank=False, verbose_name="Stock")


    def __str__(self):
        return self.name

    class Meta:
        db_table = "Products"
        verbose_name = "Product"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.id})
