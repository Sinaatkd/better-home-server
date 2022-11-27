from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from api_v1_module.serializers import (
    SendVerificationCodeSerializer,
    SignInSerializer)

from account_module.models import VerificationCode

client = Client()
User = get_user_model()


class SendVerificationCodeTest(TestCase):
    def test_correct_request(self):
        test_phone_number = 9100000000
        payload = {'phone_number': test_phone_number}
        res = client.post(reverse('send_verification_code_api'), data=payload)
        serializer = SendVerificationCodeSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            self.assertEqual(res.json(), serializer.data)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_incorrect_request(self):
        res = client.post(reverse('send_verification_code_api'))
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


class SignInTest(TestCase):
    def setUp(self) -> None:
        self.phone_number = 9120000000
        self.user = User.objects.get_or_create(phone_number=self.phone_number)
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
