from django.urls import path

from .views import SendVerificationCodeAPI

urlpatterns = [
    path('auth/send-verification-code/', SendVerificationCodeAPI.as_view(), name='SendVerificationCodeAPI')
]