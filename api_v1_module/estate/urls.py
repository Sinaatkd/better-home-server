from django.urls import path, include

from rest_framework.routers import SimpleRouter 

from .views import EstatesViewSet

router = SimpleRouter()
router.register('', EstatesViewSet)

urlpatterns = [
    path('', include(router.urls))
]