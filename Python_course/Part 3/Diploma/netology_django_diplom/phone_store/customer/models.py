from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from shop.models import Product


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    products_in_cart = models.ManyToManyField(Product, blank=True,
                                              related_name='customers',
                                              through='ProductCustomerCart')

    def __str__(self):
        return self.user.get_username()


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE,
                                 related_name='orders')
    products = models.ManyToManyField(Product, through='ProductCustomer')

    def __str__(self):
        order_list = []
        for product in self.orders.all():
            order_list.append(f'{product.qty} x {product.product.name}')
        return ', '.join(order_list)


class ProductCustomerCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='cart')
    qty = models.IntegerField(validators=[MinValueValidator(1)])

    def sum_price(self):
        return self.qty * self.product.price

    def __str__(self):
        return f'{self.qty} X {self.product.name}'


class ProductCustomer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='orders')
    qty = models.IntegerField(validators=[MinValueValidator(1)])



