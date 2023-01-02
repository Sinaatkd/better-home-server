from django.contrib.auth import get_user_model

from rest_framework import serializers

from estate_module.models import Estate


User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('last_login', 'password', 'is_superuser', 'is_staff', 'date_joined', 'groups', 'user_permissions')


class AddToEstateFavSerializer(serializers.Serializer):
    estate_id = serializers.IntegerField()
    message = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user = self.context['request'].user
        self.estate.fav_of_users.add(user)
        validated_data['status'] = 'ok'
        validated_data['message'] = 'added to user favorites'
        return validated_data
        

    def validate_estate_id(self, estate_id):
        estate = Estate.objects.filter(id=estate_id)
        if estate.exists():
            self.estate = estate.first()
            return estate_id
        raise serializers.ValidationError('آگهی پیدا نشد')



class RemoveFromEstateFavSerializer(serializers.Serializer):
    estate_id = serializers.IntegerField()
    message = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user = self.context['request'].user
        self.estate.fav_of_users.remove(user)
        validated_data['status'] = 'ok'
        validated_data['message'] = 'removed from user favorites'
        return validated_data
        

    def validate_estate_id(self, estate_id):
        estate = Estate.objects.filter(id=estate_id)
        if estate.exists():
            self.estate = estate.first()
            return estate_id
        raise serializers.ValidationError('آگهی پیدا نشد')