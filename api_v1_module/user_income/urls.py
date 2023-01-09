from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import UserIncomeViewSet


router = SimpleRouter()
router.register('', UserIncomeViewSet, basename='UserIncome')

urlpatterns = [
    path('', include(router.urls)),
]