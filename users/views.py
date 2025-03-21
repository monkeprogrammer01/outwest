from datetime import datetime, timedelta
from xml.sax.handler import property_dom_node
import os
from django.contrib.auth import authenticate
from django.template.loader import render_to_string
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from payments.models import OrderItem
from products.serializers import ProductSerializer
from telegram_app.order_message import send_telegram_message
from .models import User, Customer
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.shortcuts import redirect, render
from . serializers import RegistrationSerializer, LoginSerializer, CustomerSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from products.models import Basket, Product
import jwt
from django.conf import settings

load_dotenv()

def send_confirmation_email(user, request):
    token = jwt.encode({"id": user.pk, "exp": datetime.now() + timedelta(minutes=5)}, settings.SECRET_KEY, algorithm='HS256')
    uid = urlsafe_base64_encode(str(user.pk).encode())
    confirm_url = f"http://localhost:8000/user/email/confirm/{uid}/{token}/"
    subject = "Подтвердите ваш email"
    message = render_to_string("users/email_confirmation.html", {
        "confirm_url": confirm_url
    })
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=message)

def email_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            if payload['id'] == user.pk:
                user.email_verified = True
                user.save()
                messages.success(request, "Ваш email успешно подтверждён!")
                return render(request, 'users/email_confirmation.html')
            else:
                messages.error(request, "Невалидная ссылка подтверждения!")
                return render(request, 'users/email_confirmation.html')
        except jwt.ExpiredSignatureError:
            messages.error(request, "Срок действия ссылки истек!")
            return render(request, 'users/email_confirmation.html')
        except jwt.InvalidTokenError:
            messages.error(request, "Невалидная ссылка подтверждения!")
            return render(request, 'users/email_confirmation.html')
    except Exception as e:
        messages.error(request, "Ошибка при подтверждении email!")
        return redirect('users/login')



class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if User.objects.filter(email=user.get('email')).exists():
            return Response({"detail": "This email already exists!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_confirmation_email(user, request)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = LoginSerializer

    def post(self, request):
        user = self.request.data.get('user', {})
        email = user.get('email')
        password = user.get('password')
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # if not user.email_verified:
            #     return Response({"detail": "Please confirm your email, before logging in."})
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        basket = Basket.objects.filter(user=user)
        products = []
        final_sum = 0
        for i in basket:
            product = Product.objects.filter(id=i.product.id).first()
            final_sum += product.product_price * i.quantity
            products.append([ProductSerializer(i.product).data, i.quantity])
        user_data = {
            "id": user.id,
            "email": user.email,
            "basket": products,
            "sum": final_sum}
        return Response(user_data)

class CustomerAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer

    def post(self, request):
        user = self.request.user
        customer = request.data.get('customerData', {})
        customer['user'] = user.id
        serializer = self.serializer_class(data=customer)
        if serializer.is_valid():
            serializer.save()  # Сохраняем данные

            message = f"""Новый заказ от {user.email}
            """
            send_telegram_message(message, os.getenv("CHAT_ID"), os.getenv("BOT_TOKEN"))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = self.request.user
        addresses = Customer.objects.filter(user=user)
        serializer = CustomerSerializer(addresses, many=True)
        return Response(serializer.data)
