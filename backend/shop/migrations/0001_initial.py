# Generated by Django 3.2 on 2022-08-18 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='shops/covers/images')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='shops/profiles/images')),
                ('address', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shops/products/')),
                ('about', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('inventory', models.BigIntegerField()),
                ('cash_on_delivery_enable', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='shop.Category')),
                ('label', models.ManyToManyField(to='shop.Label')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
        ),
    ]