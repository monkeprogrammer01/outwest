from django.urls import path, include
from payments.views import OrderView
app_name = "payments"

urlpatterns = [
    path("order/", OrderView.as_view(), name="order"),
]