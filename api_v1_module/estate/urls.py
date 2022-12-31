from django.urls import path, include

from rest_framework.routers import SimpleRouter 

from .views import EstatesViewSet, GetEstatePropertiesAPI

router = SimpleRouter()
router.register('', EstatesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('properties/all/', GetEstatePropertiesAPI.as_view(), name='list-estate-properties-api')
]