from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class TestConnectionSerializer(serializers.Serializer):
    message = serializers.CharField(read_only=True, initial='connected')
    status = serializers.CharField(read_only=True, initial='ok')

