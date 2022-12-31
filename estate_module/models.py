from datetime import datetime, timedelta


import static_variables

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from base_model_module.models import BaseModel
from .managers import EstateManager

User = get_user_model()


class EstateProperty(BaseModel):
    title = models.CharField(verbose_name='عنوان', max_length=100)
    icon = models.ImageField(upload_to=static_variables.ESTATE_PROPERTY_IMAGE_UPLOAD_PATH, verbose_name='آیکن')
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'ویژگی ملک'
        verbose_name_plural = 'ویژگی های ملک'

# TODO: maybe category model added in future
# class EstateCategory(BaseModel):
#     parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True, verbose_name='والد')
#     title = models.CharField(max_length=100, verbose_name='عنوان')
#     slug = models.SlugField(unique=True, null=False, editable=False)

#     def __str__(self):
#         return self.title

#     class Meta:
#         #enforcing that there can not be two categories under a parent with same slug
#         unique_together = ('slug', 'parent',)
#         verbose_name = "دسته بندی ملک"
#         verbose_name_plural = "دسته بندی های ملک"
    

class EstateImage(BaseModel):
    image = models.ImageField(upload_to=static_variables.ESTATE_IMAGE_UPLOAD_PATH, verbose_name='تصویر ملک')
    
    def __str__(self):
        return f'{self.image}'
    
    class Meta:
        verbose_name = 'تصویر ملک'
        verbose_name_plural = 'تصویر های ملک'


class Estate(BaseModel):
    title = models.CharField(verbose_name='عنوان', max_length=300)
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    consultant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='مشاور')
    address = models.TextField(verbose_name='آدرس')
    latitude = models.FloatField(verbose_name='طول جغرافیایی')
    longitude = models.FloatField(verbose_name='عرض جغرافیایی')
    number_of_rooms = models.PositiveIntegerField(verbose_name='تعداد اتاق ها')
    floor = models.PositiveIntegerField(verbose_name='طبقه')
    estate_properties = models.ManyToManyField(EstateProperty, verbose_name='ویژگی ها', blank=True)
    meterage = models.PositiveIntegerField(verbose_name='متراژ')
    category = models.CharField(choices=static_variables.AD_CATEGORY_CHOICES, max_length=9,
                                verbose_name='دسته بندی', null=True, blank=True)
    is_special = models.BooleanField(verbose_name='آگهی ویژه', default=False)
    images = models.ManyToManyField(EstateImage, verbose_name='تصاویر', blank=True)
    price = models.BigIntegerField(verbose_name='قیمت')
    deposit = models.BigIntegerField(verbose_name='ودیعه', null=True, blank=True)
    ad_type = models.CharField(choices=static_variables.AD_TYPE_CHOICES, max_length=10, verbose_name='نوع آگهی')
    is_ladder = models.BooleanField(default=False, verbose_name='نردبون')
    last_ladder_updated_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ اپدیت نردبون', null=True, blank=True)
    build_date = models.PositiveIntegerField(verbose_name='سال ساخت', null=True, blank=True)
    fav_of_users = models.ManyToManyField(User, verbose_name='مورد علاقه', blank=True, related_name='fav_of_users')
    
    objects = EstateManager()

    def __str__(self):
        return f'{self.consultant.username} - {self.title}'

    class Meta:
        verbose_name = 'ملک'
        verbose_name_plural = 'ملک ها'


@receiver(pre_save, sender=Estate)
def set_estate_expire_date(sender, instance, *args, **kwargs):
    # set expire_date when instance created
    if instance.id is None:
        instance.expire_date = datetime.now() + timedelta(days=30)
