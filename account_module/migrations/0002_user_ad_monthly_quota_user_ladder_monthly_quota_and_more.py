# Generated by Django 4.1.3 on 2022-12-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ad_monthly_quota',
            field=models.PositiveSmallIntegerField(blank=True, default=10, null=True, verbose_name='سهمیه ماهانه آگهی'),
        ),
        migrations.AddField(
            model_name='user',
            name='ladder_monthly_quota',
            field=models.PositiveSmallIntegerField(blank=True, default=20, null=True, verbose_name='سهمیه ماهانه نردبون'),
        ),
        migrations.AddField(
            model_name='user',
            name='special_ad_monthly_quota',
            field=models.PositiveSmallIntegerField(blank=True, default=2, null=True, verbose_name='سهمیه ماهانه آگهی ویژه'),
        ),
    ]
