# Generated by Django 4.0.4 on 2022-05-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_randomurl_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomurl',
            name='url',
            field=models.URLField(default='http://127.0.0.1:8000/34caa3e347754dfad0e122b2329012f1', max_length=255, verbose_name='Url'),
        ),
    ]