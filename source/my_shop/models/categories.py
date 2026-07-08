from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False ,verbose_name="Category", unique=True)
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Categories"
        verbose_name = "Category"

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})