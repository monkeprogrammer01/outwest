from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
<<<<<<< HEAD
from products.models import Product, Basket, ProductCategory
from rest_framework.response import Response
from products.serializers import ProductSerializer, BasketSerializer, ProductCategorySerializer

class ProductCategoryAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)
=======
from products.models import Product
from rest_framework.response import Response
from products.serializers import ProductSerializer, BasketSerializer

>>>>>>> 384c2b316e6797ff86583179b1a89c4a8317a014

class ProductAPIView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class BasketAPIView(APIView):
    permission_classes = [IsAuthenticated]
<<<<<<< HEAD

    def get(self, request):
        user = request.user
        basket_items = Basket.objects.filter(user=user)
        product_ids = basket_items.values_list('product_id', flat=True)

        products = Product.objects.filter(id__in=product_ids)

        serializer = BasketSerializer(basket_items, many=True)

        return Response(serializer.data)

    def post(self, request):
        action = request.data.get('action')
        serializer = BasketSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            if action == 'decrease':
                serializer.decrease(serializer.validated_data)
                return Response({"detail": "Product quantity decreased."}, status=status.HTTP_200_OK)
            elif action == 'remove':
                serializer.remove(serializer.validated_data)
                return Response({"detail": "Product removed from basket."}, status=status.HTTP_200_OK)
            else:
                serializer.save()
                return Response({"detail": "Product added or increased."}, status=status.HTTP_201_CREATED)

=======
    def post(self, request):
        serializer = BasketSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
>>>>>>> 384c2b316e6797ff86583179b1a89c4a8317a014
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

