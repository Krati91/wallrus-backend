# Generated by Django 3.2.3 on 2021-08-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_customuser_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='platinum_royalty_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='interior_decorator',
            name='platinum_commission_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]