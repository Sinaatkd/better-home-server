from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from api_v1_module.serializers import SendVerificationCodeSerializer

client = Client()


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
        test_phone_number = 9100000000
        res = client.post(reverse('send_verification_code_api'))
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
