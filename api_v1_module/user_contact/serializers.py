from rest_framework import serializers

from user_contact_module.models import UserContact

class CreateUserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        exclude = ('is_active', 'is_delete', 'created_at', 'last_updated_time')