from django.urls import path
from users.views import RegistrationAPIView, LoginAPIView, index
app_name = "users"

urlpatterns = [
    path('', index),
    path('registration/', RegistrationAPIView.as_view(), name="registration"),
    path('login/', LoginAPIView.as_view())
]