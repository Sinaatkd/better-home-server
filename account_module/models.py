from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country_code = models.IntegerField(default=98, verbose_name='کد کشور')
    phone_number = models.BigIntegerField(verbose_name='شماره تلفن')
    is_phone_number_verified = models.BooleanField(default=False, verbose_name='شماره تلفن تایید شده/نشده')
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
