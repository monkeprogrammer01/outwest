<<<<<<< HEAD
from rest_framework import serializers
from .models import Product, Basket, ProductCategory  # Adjust the import based on your app structure

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']
=======
from cffi.model import qualify
from rest_framework import serializers
from .models import Product, Basket  # Adjust the import based on your app structure
>>>>>>> 384c2b316e6797ff86583179b1a89c4a8317a014

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ['product_image', 'product_name', 'product_description', 'product_price' ,'id', 'product_category' ]

class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ['product', 'quantity',]

=======
        fields = ['product_image', 'product_name', 'product_description', 'product_price', 'id' ]

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['product']
>>>>>>> 384c2b316e6797ff86583179b1a89c4a8317a014
    def create(self, validated_data):
        user = self.context['request'].user
        product = validated_data.get('product')
        try:
            basket = Basket.objects.get(product=product)
            basket.quantity += 1
            basket.save()
<<<<<<< HEAD

=======
>>>>>>> 384c2b316e6797ff86583179b1a89c4a8317a014
        except Basket.DoesNotExist:
            basket = Basket.objects.create(user=user, product=product, quantity=1)

        return basket
<<<<<<< HEAD

    def decrease(self, validated_data):
        user = self.context['request'].user
        product = validated_data.get('product')

        try:

            basket = Basket.objects.get(user=user, product=product)
            if basket.quantity > 1:
                basket.quantity -= 1
                basket.save()
            else:
                basket.delete()  # Удаляем, если количество становится 0
            return basket
        except Basket.DoesNotExist:
            raise serializers.ValidationError({"detail": "Product not found in basket."})

    def remove(self, validated_data):
        user = self.context['request'].user
        product = validated_data.get('product')
        try:
            basket = Basket.objects.get(user=user, product=product)
            basket.delete()
        except Basket.DoesNotExist:
            raise serializers.ValidationError({"detail": "Product not found in basket."})
=======
>>>>>>> 384c2b316e6797ff86583179b1a89c4a8317a014
