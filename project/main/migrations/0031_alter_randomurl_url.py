# Generated by Django 4.0.4 on 2022-05-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_randomurl_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomurl',
            name='url',
            field=models.URLField(default='http://127.0.0.1:8000/ce514899bfa8153c85c8d5f040dc8d2c', max_length=255, verbose_name='Url'),
        ),
    ]