from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

client = Client()

class SendVerificationCodeTest(TestCase):
    def test_correct_request(self):
        test_phone_number = 9100000000
        payload = {'phone_number': test_phone_number}
        res = client.post(reverse('SendVerificationCodeAPI'), data=payload)
        expected_response = {
            'status': 'ok',
            'message': 'code sent'
        }
        self.assertEqual(res.json(), expected_response)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_incorrect_request(self):
        test_phone_number = 9100000000
        res = client.post(reverse('SendVerificationCodeAPI'))
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
