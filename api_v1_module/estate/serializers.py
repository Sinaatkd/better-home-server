from rest_framework import serializers

from estate_module.models import Estate


class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        exclude = ('is_delete', 'created_at', 'last_updated_time')
