from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=32, default="category")

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField()
    product_image = models.ImageField(upload_to="product_images", default='media/product_images/default_product_image.png')
    product_description = models.CharField()
    product_count = models.IntegerField()
    product_price = models.IntegerField()
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
