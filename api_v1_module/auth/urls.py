from django.urls import path

from .views import SendVerificationCodeAPI, SignInAPI

urlpatterns = [
    path('send-verification-code/', SendVerificationCodeAPI.as_view(), name='send-verification-code-api'),
    path('sign-in/', SignInAPI.as_view(), name='sign-in-api'),
]