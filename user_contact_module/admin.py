from django.contrib import admin

from .models import UserContact



class UserContactAdmin(admin.ModelAdmin):
    list_display = ('consultant', 'customer', 'estate', 'status')


admin.site.register(UserContact, UserContactAdmin)
