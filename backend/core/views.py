from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CreateUserSerializer, UserSerializer
from .models import User
# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateUserSerializer
        return UserSerializer
