from django.contrib import admin

from .models import Estate, EstateImage, EstateProperty, EstateRegion


admin.site.register(Estate)
admin.site.register(EstateRegion)
admin.site.register(EstateImage)
admin.site.register(EstateProperty)