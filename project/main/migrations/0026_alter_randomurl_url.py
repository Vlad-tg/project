# Generated by Django 4.0.4 on 2022-05-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_randomurl_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomurl',
            name='url',
            field=models.URLField(default='http://127.0.0.1:8000/0dfb9704510e1200ddd564d4e6e5edc0', max_length=255, verbose_name='Url'),
        ),
    ]
