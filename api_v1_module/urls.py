from django.urls import path

from .views import (SendVerificationCodeAPI, SignInAPI, TestConnectionAPI)

urlpatterns = [
    # Authentication
    path('test-connection/', TestConnectionAPI.as_view(), name='test_connection_api'),
    path('auth/send-verification-code/', SendVerificationCodeAPI.as_view(), name='send_verification_code_api'),
    path('auth/sign-in/', SignInAPI.as_view(), name='sign_in_api'),
]