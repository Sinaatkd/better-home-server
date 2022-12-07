from django.contrib import admin

from .models import Estate, EstateCategory, EstateImage, EstateProperty


admin.site.register(Estate)
admin.site.register(EstateCategory)
admin.site.register(EstateImage)
admin.site.register(EstateProperty)