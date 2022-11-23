from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User

UserAdmin.fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "country_code", "phone_number", "is_phone_number_verified")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
)

UserAdmin.list_display = ('username', 'country_code', 'phone_number',
                          'is_phone_number_verified', 'first_name', 'last_name',
                          'is_staff', 'is_active')

admin.site.register(User, UserAdmin)