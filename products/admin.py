from django.contrib import admin
from products.models import Product, ProductCategory, Basket, ProductImage

# Register your models here.


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)
admin.site.register(ProductImage)
