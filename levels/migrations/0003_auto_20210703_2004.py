# Generated by Django 3.2.3 on 2021-07-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0002_auto_20210615_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commissiongroup',
            name='end_point',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='royaltygroup',
            name='end_point',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]