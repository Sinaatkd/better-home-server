# Generated by Django 4.1.3 on 2022-12-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_module', '0007_estate_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='last_ladder_updated_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ اپدیت نردبون'),
        ),
    ]