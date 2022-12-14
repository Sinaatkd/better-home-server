from django.db import models


class BaseModelManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(is_delete=False)

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='فعال بودن / نبودن')
    is_delete = models.BooleanField(default=False, verbose_name='حدف شده / نشده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    last_updated_time = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین اپدیت')

    objects = BaseModelManager()
    
    class Meta:
        abstract = True
