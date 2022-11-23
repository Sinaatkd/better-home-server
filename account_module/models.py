from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country_code = models.IntegerField(default=98, verbose_name='کد کشور')
    phone_number = models.BigIntegerField(verbose_name='شماره تلفن')
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
