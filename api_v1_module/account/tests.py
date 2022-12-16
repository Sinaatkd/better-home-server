from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from account_module.models import VerificationCode

client = Client()
User = get_user_model()


class GetAuthenticatedUserTest(TestCase):
    def setUp(self) -> None:
        test_phone_number = 9122344321
        self.user = User.objects.create_user(username='user', password='password', phone_number=test_phone_number)
        self.verification_code = VerificationCode.objects.create_verification_code(user=self.user)
        payload = {
            'phone_number': self.user.phone_number,
            'verification_code': self.verification_code.code
        } 
        res = client.post(reverse('sign-in-api'), data=payload)
        self.token = res.json()['token']
    
    def test_authorized(self):
        headers = {
            'HTTP_AUTHORIZATION': f'Bearer {self.token}'
        }
        res = client.get(reverse('get-authenticated-user-api'), **headers)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_unauthorized(self):
        res = client.get(reverse('get-authenticated-user-api'))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    
