import static_variables

from django.db import models

from base_model_module.models import BaseModel
from django.contrib.auth import get_user_model


User = get_user_model()


class EstateProperty(BaseModel):
    title = models.CharField(verbose_name='عنوان', max_length=100)
    icon = models.ImageField(upload_to=static_variables.ESTATE_PROPERTY_IMAGE_UPLOAD_PATH, verbose_name='آیکن')
    
    class Meta:
        verbose_name = 'ویژگی ملک'
        verbose_name_plural = 'ویژگی های ملک'


class EstateCategory(BaseModel):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True, verbose_name='والد')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(unique=True, null=False, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        unique_together = ('slug', 'parent',)
        verbose_name = "دسته بندی ملک"
        verbose_name_plural = "دسته بندی های ملک"
    

class EstateImage(BaseModel):
    image = models.ImageField(upload_to=static_variables.ESTATE_IMAGE_UPLOAD_PATH, verbose_name='تصویر ملک')
    
    class Meta:
        verbose_name = 'تصویر ملک'
        verbose_name_plural = 'تصویر های ملک'


class Estate(BaseModel):
    title = models.CharField(verbose_name='عنوان', max_length=300)
    consultant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='مشاور')
    address = models.TextField(verbose_name='آدرس')
    latitude = models.FloatField(verbose_name='طول جغرافیایی')
    longitude = models.FloatField(verbose_name='عرض جغرافیایی')
    number_of_rooms = models.PositiveIntegerField(verbose_name='تعداد اتاق ها')
    floor = models.PositiveIntegerField(verbose_name='طبقه')
    estate_properties = models.ManyToManyField(EstateProperty, verbose_name='ویژگی ها')
    meterage = models.PositiveIntegerField(verbose_name='متراژ')
    category = models.ManyToManyField(EstateCategory, verbose_name='دسته بندی')
    is_special = models.BooleanField(verbose_name='آگهی ویژه', default=False)
    images = models.ManyToManyField(EstateImage, verbose_name='تصاویر')
    price = models.BigIntegerField(verbose_name='قیمت')
    deposit = models.BigIntegerField(verbose_name='ودیعه', null=True, blank=True)
    ad_type = models.CharField(choices=static_variables.AD_TYPE_CHOICES, max_length=10, verbose_name='نوع آگهی')
    expire_date = models.DateTimeField(verbose_name='تاریخ انقضا', blank=True)

    class Meta:
        verbose_name = 'ملک'
        verbose_name_plural = 'ملک ها'
