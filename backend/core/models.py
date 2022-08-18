from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.contrib.auth.hashers import make_password

# Create your models here.


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        if not password:
            raise ValueError('The given password must be set')

        user = self.model(
            phone=phone,
            email=email,
            **extra_fields
        )

        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.

        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(db_index=True, unique=True,  max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USER_CUSTOMER = "C"
    USER_VENDOR = "V"
    USER_DELIVERY = "D"
    USER_TYPE_CHOICES = [
        (USER_CUSTOMER, "Customer"),
        (USER_VENDOR, "Vendor"),
        (USER_DELIVERY, "Delivery Boy")
    ]
    user_type = models.CharField(
        max_length=1, choices=USER_TYPE_CHOICES, default=USER_CUSTOMER)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
