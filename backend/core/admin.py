from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _


from .models import User


# Register your models here.

# admin.site.register(User)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    readonly_fields = ["date_joined"]
    fieldsets = (
        (None, {'fields': ("phone", 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', "email")}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("phone", 'email', 'password1', 'password2', "first_name", "last_name"),
        }),
    )
    list_display = ("phone", 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ("phone", 'first_name', 'last_name', 'email')
    ordering = ("phone", 'email')
