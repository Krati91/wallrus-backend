# Generated by Django 3.2.3 on 2021-08-14 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designs', '0009_designtag_designs_des_name_fa1665_idx'),
        ('product', '0003_application_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sku', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('material', models.CharField(max_length=255)),
                ('cost', models.IntegerField()),
                ('views', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['name'], name='product_tag_name_bf4b57_idx'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.application'),
        ),
        migrations.AddField(
            model_name='product',
            name='design',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designs.design'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='product.Tag'),
        ),
    ]