from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .filters import EstateFilter
from .serializers import EstateSerializer, EstateCreateUpdateSerializer, EstatePropertySerializer
from .permissions import IsConsultantUser, IsOwnerEstateAd

from estate_module.models import Estate, EstateProperty


class EstatesViewSet(ModelViewSet):
    filterset_class = EstateFilter
    queryset = Estate.objects.active_estates()
    ordering_fields = ['is_special', 'last_ladder_updated_time', 'is_ladder']
    search_fields = ['title', 'address']

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsConsultantUser]
        if self.action in ['update', 'destroy']:
            permission_classes = [IsAuthenticated, IsConsultantUser, IsOwnerEstateAd]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return EstateCreateUpdateSerializer
        return EstateSerializer


class GetEstatePropertiesAPI(ListAPIView):
    queryset = EstateProperty.objects.all()
    serializer_class = EstatePropertySerializer