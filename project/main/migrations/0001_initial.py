# Generated by Django 4.0.4 on 2022-05-17 17:48

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
            name='RandomUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
                ('url', models.URLField(max_length=255, verbose_name='Url')),
            ],
        ),
        migrations.CreateModel(
            name='Tiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
                ('size_thumbnail', models.CharField(blank=True, max_length=10, null=True, verbose_name='Size thumbnail')),
                ('url_original_image', models.URLField(blank=True, max_length=255, null=True, verbose_name='Original image (url)')),
                ('random_expiring_url', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.randomurl', verbose_name='Random expiring url')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('tiers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tiers', verbose_name='Tier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
        ),
    ]