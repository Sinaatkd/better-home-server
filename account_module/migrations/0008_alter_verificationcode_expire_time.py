# Generated by Django 4.1.3 on 2022-12-02 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0007_user_is_consultant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcode',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 16, 28, 13, 818301), verbose_name='تاریخ انقضا'),
        ),
    ]
