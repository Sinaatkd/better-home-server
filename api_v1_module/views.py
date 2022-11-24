from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (SendVerificationCodeSerializer)


class SendVerificationCodeAPI(GenericAPIView):
    serializer_class = SendVerificationCodeSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({'status': 'ok', 'message': 'code sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
