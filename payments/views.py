from django.shortcuts import render
from django.http import JsonResponse
import hmac
import hashlib

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from payments.models import Order, OrderItem
from payments.serializers import OrderSerializer
from products.models import Basket


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        basket_items = Basket.objects.filter(user=user)
        order = Order(customer=user, total_price=0)
        order_items = []
        total_price = 0
        for item in basket_items:
            total = item.quantity * item.product.product_price
            total_price += total
            order_items.append(OrderItem(order=order, product=item.product, quantity=item.quantity, price=total))

        order.total_price = total_price
        order.save()
        OrderItem.objects.bulk_create(order_items)
        basket_items.delete()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)