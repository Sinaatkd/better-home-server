from django.contrib.auth import get_user_model

from rest_framework import serializers
from estate_module.models import Estate


User = get_user_model()


class TestConnectionSerializer(serializers.Serializer):
    message = serializers.CharField(read_only=True, initial='connected')
    status = serializers.CharField(read_only=True, initial='ok')


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        exclude = ('is_delete', 'created_at', 'last_updated_time')
