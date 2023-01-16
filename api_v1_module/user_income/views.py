from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import UserIncomeCreateEditSerializer, UserIncomeSerializer, UserIncomeGeneralStatsSerializer

from user_income_module.models import UserIncome

from user_income_module.utils import calculate_income_general_stats

class UserIncomeViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return UserIncomeCreateEditSerializer
        return UserIncomeSerializer

    def get_queryset(self):
        q = UserIncome.objects.filter(user=self.request.user)
        return q


class UserIncomeGeneralStatsAPI(GenericAPIView):
    serializer_class = UserIncomeGeneralStatsSerializer
    
    def get(self, request):
        queryset = UserIncome.objects.filter(user=request.user)

        sum_of_incomes, this_month_income, progress = calculate_income_general_stats(queryset)
        
        res = {
            'sum_of_incomes': sum_of_incomes,
            'this_month_income': this_month_income,
            'progress': progress,
        }
        return Response(res, status=status.HTTP_200_OK)