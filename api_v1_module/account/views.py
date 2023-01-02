from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework import status

from ..estate.serializers import EstateSerializer
from rest_framework.response import Response

from ..estate.filters import EstateFilter
from estate_module.models import Estate

from .serializers import UserSerializer, AddToEstateFavSerializer, RemoveFromEstateFavSerializer

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


class AddToUserEstateFavAPI(GenericAPIView):
    serializer_class = AddToEstateFavSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    


class RemoveFromUserEstateFavAPI(GenericAPIView):
    serializer_class = RemoveFromEstateFavSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)