from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('last_login', 'password', 'is_superuser', 'is_staff', 'date_joined', 'groups', 'user_permissions')

