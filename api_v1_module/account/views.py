from rest_framework.generics import RetrieveAPIView, ListAPIView

from ..estate.serializers import EstateSerializer
from ..estate.filters import EstateFilter
from estate_module.models import Estate

from .serializers import UserSerializer

class GetAuthenticatedUserAPI(RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user


class GetFavEstatesAPI(ListAPIView):
    serializer_class = EstateSerializer
    filterset_class = EstateFilter
    ordering_fields = ['is_special', 'last_ladder_updated_time', 'is_ladder']
    search_fields = ['title', 'address']
    
    def get_queryset(self):
        user = self.request.user
        estates = Estate.objects.filter(fav_of_users__in=[user])
        return estates