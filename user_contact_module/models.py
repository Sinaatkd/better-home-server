import static_variables

from django.db import models

from base_model_module.models import BaseModel

from account_module.models import User
from estate_module.models import Estate



class UserContact(BaseModel):
    consultant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='مشاور', related_name='consultant')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='مشتری', related_name='customer')
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, verbose_name='ملک')
    status = models.CharField(choices=static_variables.USER_CONTACT_STATUS, max_length=20, verbose_name='وضعیت')

    
    def __str__(self):
        return f'{self.consultant} - {self.customer}'
    
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'
