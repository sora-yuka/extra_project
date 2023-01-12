from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductAPIView, CategoryAPIView


router = DefaultRouter()
router.register("", ProductAPIView)
router.register("category", CategoryAPIView)


urlpatterns = [
    # path("example/", get_example),
    path("", include(router.urls)),
]