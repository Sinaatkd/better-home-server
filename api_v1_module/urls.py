from django.urls import path

from .views import SendVerificationCodeAPI

urlpatterns = [
    # Authentication
    path('auth/send-verification-code/', SendVerificationCodeAPI.as_view(), name='send_verification_code'),
]