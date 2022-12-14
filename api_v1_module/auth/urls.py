from django.urls import path

from .views import SendVerificationCodeAPI, SignInAPI

urlpatterns = [
    path('send-verification-code/', SendVerificationCodeAPI.as_view(), name='send_verification_code_api'),
    path('sign-in/', SignInAPI.as_view(), name='sign_in_api'),
]