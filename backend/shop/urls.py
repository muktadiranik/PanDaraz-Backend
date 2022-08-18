from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()

router.register("products", views.ProductViewSet, basename="products")
router.register("shops", views.ShopViewSet, basename="shops")
router.register("labels", views.LabelViewSet, basename="labels")
router.register("categories", views.CategoryViewSet, basename="categories")

shops_router = routers.NestedDefaultRouter(router, "shops", lookup="shop")
shops_router.register("products", views.ShopProductViewSet,
                      basename="shop-products")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(shops_router.urls))
]
