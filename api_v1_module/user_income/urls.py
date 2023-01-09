from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import UserIncomeViewSet, UserIncomeGeneralStatsAPI


router = SimpleRouter()
router.register('', UserIncomeViewSet, basename='UserIncome')

urlpatterns = [
    path('', include(router.urls)),
    path('general/stats/', UserIncomeGeneralStatsAPI.as_view(), name='general-stats'),
]