# Generated by Django 4.0.4 on 2022-05-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_randomurl_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomurl',
            name='url',
            field=models.URLField(default='http://127.0.0.1:8000/a7a55172ee58d05860095b69d340eb8c', max_length=255, verbose_name='Url'),
        ),
    ]