from rest_framework.generics import ListAPIView

from .filters import EstateFilter
from .serializers import EstateSerializer

from estate_module.models import Estate


class GetEstatesAPI(ListAPIView):
    serializer_class = EstateSerializer
    filterset_class = EstateFilter
    queryset = Estate.objects.active_estates()
    ordering_fields = ['is_special', 'last_ladder_updated_time', 'is_ladder']
    search_fields = ['title', 'address']
