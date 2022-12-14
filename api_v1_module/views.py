from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import TestConnectionSerializer



class TestConnectionAPI(GenericAPIView, RetrieveModelMixin):
    permission_classes = [AllowAny]
    serializer_class = TestConnectionSerializer

    def get(self, request):
        return Response({'message': 'connected', 'status': 'ok'}, status.HTTP_200_OK)
