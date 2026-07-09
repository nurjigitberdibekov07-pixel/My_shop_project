from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(
        'my_shop.Products',
        through='IntermediateTable',
        through_fields=('order', 'product'),
        related_name='orders',
    )


class IntermediateTable(models.Model):
    product = models.ForeignKey('my_shop.Products', on_delete=models.CASCADE, related_name='order_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    count = models.IntegerField(default=0)

