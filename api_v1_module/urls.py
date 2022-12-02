from django.urls import path

from .views import (SendVerificationCodeAPI, SignInAPI, TestConnectionAPI,
                    GetAuthenticatedUserAPI)

urlpatterns = [
    path('test-connection/', TestConnectionAPI.as_view(), name='test_connection_api'),
    
    # Authentication
    path('auth/send-verification-code/', SendVerificationCodeAPI.as_view(), name='send_verification_code_api'),
    path('auth/sign-in/', SignInAPI.as_view(), name='sign_in_api'),
    path('account/', GetAuthenticatedUserAPI.as_view(), name='get_authenticated_user_api'),
]