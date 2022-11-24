from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as response_status_code

from .serializers import (SendVerificationCodeSerializer)

class SendVerificationCodeAPI(APIView):
    def post(self, request):
        serializer = SendVerificationCodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({'status': 'ok', 'message': 'code sent'}, status=response_status_code.HTTP_200_OK)
        return Response(serializer.errors, status=response_status_code.HTTP_400_BAD_REQUEST)
