from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from products.models import Product
from rest_framework.response import Response
from products.serializers import ProductSerializer, BasketSerializer


class ProductAPIView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class BasketAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = BasketSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

