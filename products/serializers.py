from cffi.model import qualify
from rest_framework import serializers
from .models import Product, Basket  # Adjust the import based on your app structure

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_image', 'product_name', 'product_description', 'product_price', 'id' ]

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['product']
    def create(self, validated_data):
        user = self.context['request'].user
        product = validated_data.get('product')
        try:
            basket = Basket.objects.get(product=product)
            basket.quantity += 1
            basket.save()
        except Basket.DoesNotExist:
            basket = Basket.objects.create(user=user, product=product, quantity=1)

        return basket
