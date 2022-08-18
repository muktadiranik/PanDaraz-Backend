from turtle import tilt
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from . import models


class LabelSerializer(ModelSerializer):
    class Meta:
        model = models.Label
        fields = ["id", "title"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["id", "title"]


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(many=True)
    label = LabelSerializer(many=True)

    class Meta:
        model = models.Product
        fields = ["id", "shop", "title", "created_at", "image", "about", "category",
                  "label", "price", "discount", "inventory", "cash_on_delivery_enable"]


class CreateProductSerializer(ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=models.Category.objects.all(), many=True)
    label = serializers.PrimaryKeyRelatedField(
        queryset=models.Label.objects.all(), many=True)

    class Meta:
        model = models.Product
        fields = ["id", "title", "image", "about", "category",
                  "label", "price", "discount", "inventory", "cash_on_delivery_enable"]

    def create(self, validated_data):
        shop_id = self.context["shop_id"]
        title = validated_data["title"]
        image = validated_data["image"]
        about = validated_data["about"]
        price = validated_data["price"]
        discount = validated_data["discount"]
        inventory = validated_data["inventory"]
        cash_on_delivery_enable = validated_data["cash_on_delivery_enable"]
        category = validated_data["category"]
        label = validated_data["label"]
        instance = models.Product.objects.create(shop_id=shop_id,
                                                 title=title,
                                                 image=image,
                                                 about=about,
                                                 price=price,
                                                 discount=discount,
                                                 inventory=inventory,
                                                 cash_on_delivery_enable=cash_on_delivery_enable
                                                 )
        instance.category.set(category)
        instance.label.set(label)
        return instance


class ShopSerializer(ModelSerializer):
    product_set = ProductSerializer(many=True)

    class Meta:
        model = models.Shop
        fields = ["id", "user", "title", "cover_image", "profile_image",
                  "address", "about", "opening_time", "closing_time", "product_set"]


class CreateShopSerializer(ModelSerializer):
    class Meta:
        model = models.Shop
        fields = ["id", "user", "title", "cover_image", "profile_image",
                  "address", "about", "opening_time", "closing_time"]


class UpdateShopSerializer(ModelSerializer):
    product_set = CreateProductSerializer(many=True)

    class Meta:
        model = models.Shop
        fields = ["title", "cover_image", "profile_image",
                  "address", "about", "opening_time", "closing_time", "product_set"]
