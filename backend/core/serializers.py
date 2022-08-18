from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import User


class UserSerializer(ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ["id", "phone", "email", "password", "first_name",
                  "last_name", "phone", "is_superuser", "is_staff"]


class CreateUserSerializer(ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ["id", "phone", "email", "password", "first_name",
                  "last_name", "phone", "is_superuser", "is_staff"]

    def save(self, **kwargs):
        phone = self.validated_data["phone"]
        email = self.validated_data["email"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        password = make_password(self.validated_data["password"])
        self.instance = User.objects.create(
            phone=phone,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_superuser=False,
            is_staff=False,
        )
        return self.instance
