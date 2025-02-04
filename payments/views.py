from django.shortcuts import render
from django.http import JsonResponse
import hmac
import hashlib

def notification_handler(request):
    if request.method == "POST":
        # Получите данные уведомления
        data = request.POST

        # Проверьте подпись
        notification_secret = "your_notification_secret"
        signature = data.get("sha1_hash")
        body = "".join([f"{key}={value}&" for key, value in data.items() if key != "sha1_hash"]).strip("&")
        calculated_signature = hmac.new(notification_secret.encode(), body.encode(), hashlib.sha1).hexdigest()

        if signature != calculated_signature:
            return JsonResponse({"status": "error", "message": "Invalid signature"}, status=400)

        # Обработайте данные (например, сохраните статус платежа)
        # Пример: статус = data["unaccepted"]

        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)
