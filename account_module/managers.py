from random import randint

from datetime import timedelta, datetime

from django.db import models
from django.db.models import Q
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def get_or_create(self, phone_number, **extra_fields):
        '''It checks whether there is a user with the entered phone number or not, 
        if there is no user with the entered phone number, it creates one
        '''
        user = self.get_queryset().filter(phone_number=phone_number, **extra_fields).first()
        if user is not None:
            return user
        user = self.model(phone_number=phone_number, username=str(phone_number), **extra_fields)
        user.set_password(str(phone_number))
        user.save()
        return user
    
    def search_user_by_username_or_phone_number(self, search: str):
        if search[0] == '0':
            search = search.replace('0', '', 1)
        lookup = Q(username__icontains=search) | Q(phone_number__icontains=search)
        return self.get_queryset().filter(lookup).distinct()

        
class VerificationCodeManager(models.Manager):
    def create_verification_code(self, user):
        code = str(randint(0, 9999)).zfill(4)
        expire_time = datetime.now() + timedelta(minutes=2)
        return self.get_queryset().create(user=user, code=code, expire_time=expire_time)
    
    def check_code_has_expired(self, verification_code, user):
        return not self.get_queryset().filter(code=verification_code, user=user, expire_time__gt=datetime.now()).exists()