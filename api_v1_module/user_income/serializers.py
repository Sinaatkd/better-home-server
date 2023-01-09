from rest_framework import serializers

from user_income_module.models import UserIncome
from api_v1_module.estate.serializers import EstateSerializer
from api_v1_module.account.serializers import UserSerializer



class UserIncomeSerializer(serializers.ModelSerializer):
    estate = EstateSerializer(many=False)
    user = UserSerializer(many=False)
    
    class Meta:
        model = UserIncome
        exclude = ('is_active', 'is_delete', 'last_updated_time')

class UserIncomeCreateEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIncome
        exclude = ('is_active', 'is_delete', 'last_updated_time')



class UserIncomeGeneralStatsSerializer(serializers.Serializer):
    sum_of_incomes = serializers.IntegerField()
    this_month_income = serializers.IntegerField()
    progress = serializers.IntegerField()