from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False ,verbose_name="Категория", unique=True)
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание категории")

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        db_table = "Категории"
        verbose_name = "категория"

class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Название")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey("my_shop.Categories", on_delete=models.RESTRICT, related_name="products", null=False, blank=False,)
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    image = models.URLField(max_length=300, null=False, blank=False)
    stock = models.IntegerField(default=0, null=False, blank=False, verbose_name="Остаток")


    def __str__(self):
        return self.name

    class Meta:
        db_table = "Продукты"
        verbose_name = "Продукт"


