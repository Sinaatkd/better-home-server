from django.contrib import admin

from .models import Estate, EstateImage, EstateProperty


admin.site.register(Estate)
admin.site.register(EstateImage)
admin.site.register(EstateProperty)