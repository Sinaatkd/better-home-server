from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status

from .serializers import (SendVerificationCodeSerializer, SignInSerializer,
                          TestConnectionSerializer,)



class TestConnectionAPI(GenericAPIView, RetrieveModelMixin):
    serializer_class = TestConnectionSerializer

    def get(self, request):
        return Response({'message': 'connected', 'status': 'ok'}, status.HTTP_200_OK)

class SendVerificationCodeAPI(GenericAPIView):
    serializer_class = SendVerificationCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInAPI(GenericAPIView):
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
