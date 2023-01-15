from django.urls import path, include

from rest_framework.routers import SimpleRouter 

from .views import EstatesViewSet, GetEstatePropertiesAPI, UploadEstateImageAPI, GetEstateRegionsAPI

router = SimpleRouter()
router.register('', EstatesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/estate-image/', UploadEstateImageAPI.as_view(), name='upload-estate-image-api'),
    path('properties/all/', GetEstatePropertiesAPI.as_view(), name='list-estate-properties-api'),
    path('regions/all/', GetEstateRegionsAPI.as_view(), name='list-estate-regions-api'),
]