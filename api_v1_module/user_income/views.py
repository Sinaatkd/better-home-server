from rest_framework.viewsets import ModelViewSet

from .serializers import UserIncomeCreateEditSerializer, UserIncomeSerializer

from user_income_module.models import UserIncome

class UserIncomeViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return UserIncomeCreateEditSerializer
        return UserIncomeSerializer

    def get_queryset(self):
        q = UserIncome.objects.filter(user=self.request.user)
        return q