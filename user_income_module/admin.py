from django.contrib import admin

from .models import UserIncome

class UserIncomeAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'estate', 'amount')


admin.site.register(UserIncome, UserIncomeAdmin)
