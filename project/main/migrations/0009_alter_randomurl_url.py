# Generated by Django 4.0.4 on 2022-05-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_randomurl_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomurl',
            name='url',
            field=models.URLField(default='http://127.0.0.1:8000/d77893fe1ec062b91723c5689501fc99', max_length=255, verbose_name='Url'),
        ),
    ]