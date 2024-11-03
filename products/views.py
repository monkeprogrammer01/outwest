from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from products.models import Product
from rest_framework.response import Response
from products.serializers import ProductSerializer

class ProductAPIView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
