# Generated by Django 4.1.3 on 2023-01-09 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_module', '0012_estate_fav_of_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='is_publish',
            field=models.BooleanField(default=False, verbose_name='انتشار نهایی'),
        ),
    ]
