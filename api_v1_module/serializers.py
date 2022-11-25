from django.contrib.auth import get_user_model

from rest_framework import serializers

from account_module.models import VerificationCode

User = get_user_model()


class SendVerificationCodeSerializer(serializers.Serializer):
    country_code = serializers.IntegerField(initial=98, default=98)
    phone_number = serializers.IntegerField()
    status = serializers.CharField(read_only=True)
    message = serializers.CharField(read_only=True)

    def create(self, validated_data):
        verification_code = VerificationCode.objects.create_verification_code(user=self.user)
        # TODO: send sms
        validated_data['message'] = 'code sent'
        validated_data['status'] = 'ok'
        return validated_data

    def validate_phone_number(self, phone_number):
        user = User.objects.get_or_create(phone_number=phone_number)
        self.user = user
        return phone_number
