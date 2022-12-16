from django.urls import path, include

from .views import TestConnectionAPI


urlpatterns = [
    path('test-connection/', TestConnectionAPI.as_view(), name='test-connection-api'),
    path('auth/', include('api_v1_module.auth.urls'), name='api-v1-auth'),
    path('account/', include('api_v1_module.account.urls'), name='api-v1-account'),
    path('estates/', include('api_v1_module.estate.urls'), name='api-v1-estate'),
]