from dotenv import load_dotenv

from telegram_app.order_message import send_telegram_message
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from payments.models import Order, OrderItem
from payments.serializers import OrderSerializer
from products.models import Basket
import os

load_dotenv()

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
        order_items = OrderItem.objects.filter(order=order).select_related('product')
        message = f"""
Новый заказ!
Клиент: {user.email}
Товар: {[{item.product.product_name, item.quantity} for item in order_items]}
Сумма: {order.total_price}"""
        send_telegram_message(message, os.getenv("CHAT_ID"), os.getenv("BOT_TOKEN"))
        return Response(serializer.data, status=status.HTTP_201_CREATED)