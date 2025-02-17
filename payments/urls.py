from django.urls import path, include
from payments.views import OrderView, OrderListView

app_name = "payments"

urlpatterns = [
    path("order/", OrderView.as_view(), name="order"),
    path("get-my-orders/", OrderListView.as_view(), name="get-my-orders"),
]