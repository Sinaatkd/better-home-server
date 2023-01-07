from django.contrib import admin

from .models import UserContact



class UserContactAdmin(admin.ModelAdmin):
    list_display = ('consultant','customer_phone_number', 'estate', 'status')


admin.site.register(UserContact, UserContactAdmin)
