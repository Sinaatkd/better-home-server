from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .filters import EstateFilter
from .serializers import (  EstateSerializer, EstateCreateUpdateSerializer,
                            EstatePropertySerializer, EstateImageSerializer,
                            EstateRegionSerializer)
from .permissions import IsConsultantUser, IsOwnerEstateAd

from estate_module.models import Estate, EstateProperty, EstateImage, EstateRegion


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


class UploadEstateImageAPI(CreateAPIView):
    serializer_class = EstateImageSerializer
    queryset = EstateImage.objects.all()
    

class GetEstateRegionsAPI(ListAPIView):
    queryset = EstateRegion.objects.all()
    serializer_class = EstateRegionSerializer


class GetSimilarEstates(ListAPIView):
    serializer_class = EstateSerializer
    
    def get_queryset(self):
        selected_estate_pk = self.kwargs.get('pk')
        selected_estate = Estate.objects.filter(pk=selected_estate_pk).first()
        if selected_estate is not None:
            meterage_percent = selected_estate.meterage / 100 * 15
            meterage_range = [selected_estate.meterage - meterage_percent, selected_estate.meterage + meterage_percent]

            price_percent = selected_estate.price / 100 * 15
            price_range = [selected_estate.price - price_percent, selected_estate.price + price_percent]

            queryset = Estate.objects.filter(region=selected_estate.region, meterage__range=meterage_range, price__range=price_range)
            return queryset
        return []
