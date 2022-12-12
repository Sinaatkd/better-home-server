from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .filters import EstateFilter
from .serializers import (TestConnectionSerializer, )

from estate_module.models import Estate


class TestConnectionAPI(GenericAPIView, RetrieveModelMixin):
    permission_classes = [AllowAny]
    serializer_class = TestConnectionSerializer

    def get(self, request):
        return Response({'message': 'connected', 'status': 'ok'}, status.HTTP_200_OK)


class GetEstatesAPI(ListAPIView):
    serializer_class = EstateSerializer
    filterset_class = EstateFilter
    queryset = Estate.objects.active_estates()
    ordering_fields = ['is_special', 'last_ladder_updated_time', 'is_ladder']
    search_fields = ['title', 'address']
