# Generated by Django 4.0.4 on 2022-05-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_randomurl_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomurl',
            name='url',
            field=models.URLField(default='http://127.0.0.1:8000/6928bfe4eb0ee098731fdf5a837b3aad', max_length=255, verbose_name='Url'),
        ),
    ]
