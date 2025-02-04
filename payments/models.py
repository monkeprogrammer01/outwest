from django.core.validators import MaxValueValidator
from django.db import models
from users.models import User
from products.models import Product

class Order(models.Model):
    customer =  models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MaxValueValidator(200000)])

    def __str__(self):
        return self.customer.email

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.order.customer.email