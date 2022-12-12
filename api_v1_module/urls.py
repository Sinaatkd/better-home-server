from django.urls import path, include

from .views import TestConnectionAPI


urlpatterns = [
    path('test-connection/', TestConnectionAPI.as_view(), name='test_connection_api'),
    path('auth/', include('api_v1_module.auth.urls'), name='api_v1_auth'),
    path('account/', include('api_v1_module.account.urls'), name='api_v1_account'),
    path('estates/', include('api_v1_module.estate.urls'), name='api_v1_estate'),
]