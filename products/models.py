from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=32, default="category")

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    product_description = models.CharField(max_length=64)
    product_count = models.IntegerField()
    product_price = models.IntegerField()
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/", )

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


