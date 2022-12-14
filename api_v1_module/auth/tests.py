from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from .serializers import (
    SendVerificationCodeSerializer,
    SignInSerializer)

from account_module.models import VerificationCode

client = Client()
User = get_user_model()


class SendVerificationCodeTest(TestCase):
    def setUp(self) -> None:
        self.test_phone_number = 9100000000
        self.payload = {'phone_number': self.test_phone_number}
    
    def test_correct_request(self):
        res = client.post(reverse('send_verification_code_api'), data=self.payload)
        serializer = SendVerificationCodeSerializer(data=self.payload)
        if serializer.is_valid():
            serializer.save()
            self.assertEqual(res.json(), serializer.data)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_incorrect_request(self):
        res = client.post(reverse('send_verification_code_api'))
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_inactive_account(self):
        inactive_phone_number = 9999999999
        inactive_account = User.objects.create_user(username='username', password='fldsf', phone_number=inactive_phone_number, is_active=False)
        payload = {
            'phone_number': inactive_account.phone_number
        }
        res = client.post(reverse('send_verification_code_api'), data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


class SignInTest(TestCase):
    def setUp(self) -> None:
        self.phone_number = 9120000000
        self.user = User.objects.create_user(phone_number=self.phone_number, username='username', password='password')
        self.verification_code = VerificationCode.objects.create_verification_code(user=self.user)

    def test_success_sign_in(self):
        payload = {
            'phone_number': self.phone_number,
            'verification_code': self.verification_code.code
        }
        res = client.post(reverse('sign_in_api'), data=payload)
        serializer = SignInSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_user_not_found_sign_in(self):
        not_registered_phone_number = 9212122413
        payload = {
            'phone_number': not_registered_phone_number,
            'verification_code': self.verification_code.code
        }
        res = client.post(reverse('sign_in_api'), data=payload)
        serializer = SignInSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.json(), serializer.errors)

    def test_incorrect_verification_code(self):
        payload = {
            'phone_number': self.phone_number,
            'verification_code': 1111
        }
        res = client.post(reverse('sign_in_api'), data=payload)
        serializer = SignInSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.json(), serializer.errors)
    
    def test_inactive_account(self):
        inactive_phone_number = 9999999990
        inactive_account = User.objects.create_user(username='sign_in_inactive_user', password='fldsf', phone_number=inactive_phone_number, is_active=False)
        payload = {
            'phone_number': inactive_account.phone_number
        }
        res = client.post(reverse('send_verification_code_api'), data=payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
