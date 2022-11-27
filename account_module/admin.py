from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, VerificationCode

UserAdmin.fieldsets = (
    (None, {"fields": ("username", "password")}),
    (_("Personal info"),
     {"fields": ("first_name", "last_name", "country_code", "phone_number", "is_phone_number_verified")}),
    (
        _("Permissions"),
        {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                'is_consultant',
                "groups",
                "user_permissions",
            ),
        },
    ),
    (_("Important dates"), {"fields": ("last_login", "date_joined")}),
)

UserAdmin.list_display = ('username', 'country_code', 'phone_number',
                          'is_phone_number_verified', 'first_name', 'last_name',
                          'is_active', 'is_staff', 'is_consultant')

admin.site.register(User, UserAdmin)


class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'expire_time')


admin.site.register(VerificationCode, VerificationCodeAdmin)
