from django.db import models
from django.contrib.auth.models import AbstractUser

from base_model_module.models import BaseModel
from .managers import VerificationCodeManager, UserManager


class User(AbstractUser):
    country_code = models.IntegerField(default=98, verbose_name='کد کشور')
    phone_number = models.BigIntegerField(verbose_name='شماره تلفن', unique=True)
    is_phone_number_verified = models.BooleanField(default=False, verbose_name='شماره تلفن تایید شده / نشده')
    is_consultant = models.BooleanField(default=False, verbose_name='وضعیت مشاور بودن / نبودن')
    ad_monthly_quota = models.PositiveSmallIntegerField(verbose_name='سهمیه ماهانه آگهی', null=True, blank=True, default=10)
    ladder_monthly_quota = models.PositiveSmallIntegerField(verbose_name='سهمیه ماهانه نردبون', null=True, blank=True, default=20)
    special_ad_monthly_quota = models.PositiveSmallIntegerField(verbose_name='سهمیه ماهانه آگهی ویژه', null=True, blank=True, default=2)
    
    objects = UserManager()
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

class VerificationCode(BaseModel):
    code = models.CharField(max_length=4,verbose_name='کد تایید')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    expire_time = models.DateTimeField(verbose_name='تاریخ انقضا') # code expire after 2 minutes
    
    objects = VerificationCodeManager()
    
    def __str__(self):
        return f'{self.code} - {self.user.username}'
    
    class Meta:
        verbose_name = 'کد تایید'
        verbose_name_plural = 'کد های تایید'
    