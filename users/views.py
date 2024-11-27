from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from . serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from products.models import Basket


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
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
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    # renderer_classes = [UserJSONRenderer]  # Удалите эту строку, если она есть

    def get(self, request):
        user = self.request.user
        basket = Basket.objects.filter(user=user)
        json_data = serializers.serialize('json', basket)
        user_data = {
            "id": user.id,
            "email": user.email,
            "basket": json_data
        }
        return Response(user_data)

