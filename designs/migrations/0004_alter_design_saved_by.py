# Generated by Django 3.2.3 on 2021-06-18 15:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designs', '0003_auto_20210618_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='saved_by',
            field=models.ManyToManyField(limit_choices_to={'type': 2}, to=settings.AUTH_USER_MODEL),
        ),
    ]
