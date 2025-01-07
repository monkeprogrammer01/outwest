from django.urls import path, include
<<<<<<< HEAD
from products.views import ProductAPIView, BasketAPIView, ProductCategoryAPIView
=======
from products.views import ProductAPIView, BasketAPIView
>>>>>>> 384c2b316e6797ff86583179b1a89c4a8317a014
from django.conf import settings
from django.conf.urls.static import static
app_name = "products/"

urlpatterns = [
    path("", ProductAPIView.as_view()),
    path("add/", BasketAPIView.as_view()),
<<<<<<< HEAD
    path("mybasket/", BasketAPIView.as_view()),
    path("category/", ProductCategoryAPIView.as_view()),
=======
>>>>>>> 384c2b316e6797ff86583179b1a89c4a8317a014
]


if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

