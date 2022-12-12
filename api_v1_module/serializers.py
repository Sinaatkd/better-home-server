from django.contrib.auth import get_user_model

from rest_framework import serializers
from estate_module.models import Estate


User = get_user_model()


class TestConnectionSerializer(serializers.Serializer):
    message = serializers.CharField(read_only=True, initial='connected')
    status = serializers.CharField(read_only=True, initial='ok')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('last_login', 'password', 'is_superuser', 'is_staff', 'date_joined', 'groups', 'user_permissions')


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        exclude = ('is_delete', 'created_at', 'last_updated_time')
