# Generated by Django 3.2.3 on 2021-06-03 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.customuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interior_Decorator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.customuser')),
                ('firm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.firm')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='levels.commissiongroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.customuser')),
                ('bio', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='profile_pictures')),
                ('firm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.firm')),
                ('followers', models.ManyToManyField(to='users.Interior_Decorator')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='levels.royaltygroup')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]