# Generated by Django 4.0.4 on 2022-05-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_randomurl_validity_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomurl',
            name='url',
            field=models.URLField(default='http://127.0.0.1:8000fbbbb339decb016648f564b172593656', max_length=255, verbose_name='Url'),
        ),
    ]
