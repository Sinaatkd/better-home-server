from datetime import timedelta

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

from base_model_module.models import BaseModel

class User(AbstractUser):
    country_code = models.IntegerField(default=98, verbose_name='کد کشور')
    phone_number = models.BigIntegerField(verbose_name='شماره تلفن')
    is_phone_number_verified = models.BooleanField(default=False, verbose_name='شماره تلفن تایید شده/نشده')
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

class VerificationCode(BaseModel):
    code = models.IntegerField(verbose_name='کد تایید')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    expire_time = models.DateTimeField(default=timezone.now() + timedelta(minutes=2), verbose_name='تاریخ انقضا') # cod expire after 2 minutes
    
    def __str__(self):
        return f'{self.code} - {self.user.username}'
    
    class Meta:
        verbose_name = 'کد تایید'
        verbose_name_plural = 'کد های تایید'
    