from django.urls import path, include

from .views import (TestConnectionAPI, GetAuthenticatedUserAPI, GetEstatesAPI)

urlpatterns = [
    path('test-connection/', TestConnectionAPI.as_view(), name='test_connection_api'),
    
    # Authentication
    path('auth/', include('api_v1_module.auth.urls'), name='api_vi_auth'),

    # Account
    path('account/', GetAuthenticatedUserAPI.as_view(), name='get_authenticated_user_api'),

    # Estate
    path('estates/', GetEstatesAPI.as_view(), name='get_estate_api')
]