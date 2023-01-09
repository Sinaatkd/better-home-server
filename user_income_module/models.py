from django.db import models

from base_model_module.models import BaseModel
from estate_module.models import Estate
from account_module.models import User


class UserIncome(BaseModel):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    amount = models.PositiveBigIntegerField(verbose_name='درآمد')
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, verbose_name='ملک')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self) -> str:
        return f'{self.title} - {self.title}'

    class Meta:
        verbose_name = 'درآمد'
        verbose_name_plural = 'درآمد ها'