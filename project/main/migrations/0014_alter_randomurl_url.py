# Generated by Django 4.0.4 on 2022-05-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_randomurl_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomurl',
            name='url',
            field=models.URLField(default='http://127.0.0.1:8000/a0b3e185b7d792a670927c65a699bb6d', max_length=255, verbose_name='Url'),
        ),
    ]
