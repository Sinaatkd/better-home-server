from random import randint

from django.db import models
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

        
class VerificationCodeManager(models.Manager):
    def create_verification_code(self, user):
        code = str(randint(0, 9999)).zfill(4)
        self.get_queryset().create(user=user, code=code)