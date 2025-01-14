from django.urls import path, include
from users.views import RegistrationAPIView, LoginAPIView, ProfileAPIView, email_confirm
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "users"

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name="registration"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('profile/', ProfileAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('email/confirm/<uidb64>/<token>/', email_confirm, name='email_confirm'),
    #
    # path('login/', LoginAPIView.as_view()),
    # path('profile/', ProfileAPIView.as_view()),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]