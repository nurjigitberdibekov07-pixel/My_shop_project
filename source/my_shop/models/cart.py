from django.db import models


class Cart(models.Model):
    product = models.ForeignKey('my_shop.Products', on_delete=models.CASCADE, related_name='cart', null=True, blank=True)
    count = models.IntegerField(default=0, verbose_name='count')

    def __str__(self):
        return str(self.product)

    def total_price(self):
        return self.count * self.product.price

    class Meta:
        db_table = "Cart"
        verbose_name = "Cart"
