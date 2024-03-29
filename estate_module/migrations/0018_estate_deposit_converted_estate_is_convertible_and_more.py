# Generated by Django 4.1.3 on 2023-01-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_module', '0017_alter_estate_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='deposit_converted',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='ودیعه تغییر یافته'),
        ),
        migrations.AddField(
            model_name='estate',
            name='is_convertible',
            field=models.BooleanField(default=False, verbose_name='قابل تغییر بودن'),
        ),
        migrations.AddField(
            model_name='estate',
            name='price_converted',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='قیمت تغییر یافته'),
        ),
    ]
