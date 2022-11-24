# Generated by Django 4.1.3 on 2022-11-23 22:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0002_user_is_phone_number_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال بودن / نبودن')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حدف شده / نشده')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین اپدیت')),
                ('code', models.IntegerField(verbose_name='کد تایید')),
                ('expire_time', models.DateTimeField(default=datetime.datetime(2022, 11, 23, 22, 54, 20, 409870, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'کد تایید',
                'verbose_name_plural': 'کد های تایید',
            },
        ),
    ]