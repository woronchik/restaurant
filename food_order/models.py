from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    preparation_time = models.PositiveIntegerField()


class MenuItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    special_instructions = models.TextField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField()

    @property
    def delivery_time(self):
        max_preparation_time = max([item.product.preparation_time for item in self.menu_items.all()])
        return max_preparation_time + 30

    def update_order(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def cancel_order(self):
        self.delete()

    def update_customer_info(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()





