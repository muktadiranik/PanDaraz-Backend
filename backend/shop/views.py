from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers
# Create your views here.


class ShopViewSet(ModelViewSet):
    queryset = models.Shop.objects.prefetch_related("product_set").all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CreateShopSerializer
        if self.request.method == "PUT":
            return serializers.UpdateShopSerializer
        return serializers.ShopSerializer


class ShopProductViewSet(ModelViewSet):
    serializer_class = serializers.CreateProductSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CreateProductSerializer
        return serializers.ProductSerializer

    def get_queryset(self):
        return models.Product.objects.filter(shop_id=self.kwargs["shop_pk"])

    def get_serializer_context(self):
        return {"shop_id": self.kwargs["shop_pk"]}


class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class LabelViewSet(ModelViewSet):
    queryset = models.Label.objects.all()
    serializer_class = serializers.LabelSerializer


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
