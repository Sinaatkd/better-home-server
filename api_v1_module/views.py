from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .filters import EstateFilter
from .serializers import (SendVerificationCodeSerializer, SignInSerializer,
                          TestConnectionSerializer, UserSerializer, EstateSerializer)

from estate_module.models import Estate


class TestConnectionAPI(GenericAPIView, RetrieveModelMixin):
    permission_classes = [AllowAny]
    serializer_class = TestConnectionSerializer

    def get(self, request):
        return Response({'message': 'connected', 'status': 'ok'}, status.HTTP_200_OK)

class SendVerificationCodeAPI(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SendVerificationCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInAPI(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAuthenticatedUserAPI(RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user


class GetEstatesAPI(ListAPIView):
    permission_classes = []
    serializer_class = EstateSerializer
    filterset_class = EstateFilter
    queryset = Estate.objects.active_estates()
    ordering_fields = ['is_special', 'last_updated_time', 'is_ladder']
    search_fields = ['title', 'address']