from distutils.command.upload import upload
from django.db import models
from django.conf import settings

# Create your models here.


class Shop(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(
        upload_to="shops/covers/images", null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="shops/profiles/images", null=True, blank=True)
    address = models.CharField(max_length=255)
    about = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Label(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="shops/products/", null=True, blank=True)
    about = models.TextField()
    category = models.ManyToManyField(Category)
    label = models.ManyToManyField(Label)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(
        max_digits=4, decimal_places=2, default=00.00)
    inventory = models.BigIntegerField()
    cash_on_delivery_enable = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
