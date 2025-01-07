from django.db import models
from django.conf import settings

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма заказа"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)