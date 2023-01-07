from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import UserContactsViewSet


router = SimpleRouter()
router.register('', UserContactsViewSet, basename='UserContact')

urlpatterns = [
    path('', include(router.urls)),
]