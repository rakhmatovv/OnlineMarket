from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    description = models.TextField()
    price = models.IntegerField()
    is_new = models.BooleanField(default=False)
    is_discounted = models.BooleanField(default=False)
    category = models.ForeignKey('shop.Category', default=None, on_delete=models.CASCADE)
    brand = models.ForeignKey('shop.Brand', default=None, on_delete=models.CASCADE)
    thumb = models.ImageField(default='default.png', null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_products'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_brands'


class Slide(models.Model):
    image = models.ImageField(default='slide.jpg')


class CartItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return f"Order #{self.pk}"


class OrderProduct(models.Model):
    order = models.ForeignKey('shop.Order', on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    amount = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"{self.product} x{self.amount} - {self.order.customer.username}"




