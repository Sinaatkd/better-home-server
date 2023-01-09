from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateUserContactSerializer

from user_contact_module.models import UserContact
from ..estate.permissions import IsConsultantUser
from .permissions import IsConsultantCustomer

class UserContactsViewSet(ModelViewSet):
    serializer_class = CreateUserContactSerializer
    permission_classes = [IsAuthenticated, IsConsultantCustomer]

    def get_queryset(self):
        return UserContact.objects.filter(consultant=self.request.user)