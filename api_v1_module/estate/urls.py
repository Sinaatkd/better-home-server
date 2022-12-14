from django.urls import path

from .views import GetEstatesAPI

urlpatterns = [
    path('', GetEstatesAPI.as_view(), name='get_estate_api')
]