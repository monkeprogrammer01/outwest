from rest_framework import serializers
from .models import Product, Basket, ProductCategory  # Adjust the import based on your app structure


from cffi.model import qualify
from rest_framework import serializers
from .models import Product, Basket  # Adjust the import based on your app structure

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_image', 'product_name', 'product_description', 'product_price' ,'id', 'product_category' ]

class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ['product', 'quantity',]


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