from rest_framework import serializers
from .models import Product  # Adjust the import based on your app structure

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'