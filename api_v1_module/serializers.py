from django.contrib.auth import get_user_model

from rest_framework import serializers

from account_module.models import VerificationCode
from account_module.utils import generate_token_for_user


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


class SignInSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    country_code = serializers.CharField(default=98, initial=98)
    verification_code = serializers.CharField()
    token = serializers.CharField(read_only=True)

    def validate_phone_number(self, phone_number):
        user = User.objects.filter(phone_number=phone_number).first()
        if user is not None:
            return phone_number
        raise serializers.ValidationError('کاربری با شماره تلفن وارد شده یافت نشد')
    
    def validate_verification_code(self, verification_code):
        phone_number = self.initial_data.get('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()
        is_verification_code_expired = VerificationCode.objects.check_code_has_expired(verification_code, user)
        if is_verification_code_expired:
            raise serializers.ValidationError('کد وارد شده اشتباه است')
        return verification_code
    
    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()
        token = generate_token_for_user(user)
        validated_data['token'] = token
        return validated_data