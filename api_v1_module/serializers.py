from django.contrib.auth import get_user_model

from rest_framework import serializers

from account_module.models import VerificationCode

User = get_user_model()

class SendVerificationCodeSerializer(serializers.ModelSerializer):
    country_code = serializers.IntegerField(default=98)
    phone_number = serializers.IntegerField()

    class Meta:
        model = VerificationCode
        fields = ('phone_number', 'country_code', 'user')
        read_only_fields = ('user',)
    
    def create(self, validated_data):
        VerificationCode.objects.create_verification_code(user=self.user)
        # TODO: send sms
    
    def validate_phone_number(self, phone_number):
        user = User.objects.get_or_create(phone_number=phone_number)
        self.user = user
        return phone_number