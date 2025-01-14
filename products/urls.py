from django.urls import path, include
from products.views import ProductAPIView, BasketAPIView, ProductCategoryAPIView, get_product

from products.views import ProductAPIView, BasketAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "products/"

urlpatterns = [
    path("", ProductAPIView.as_view()),
    path("add/", BasketAPIView.as_view()),
    path("mybasket/", BasketAPIView.as_view()),
    path("category/", ProductCategoryAPIView.as_view()),
    path("<int:pk>/", get_product),
]


if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

