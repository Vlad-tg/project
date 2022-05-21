# Generated by Django 4.0.4 on 2022-05-17 18:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_customer_tiers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randomurl',
            name='slug',
        ),
        migrations.AddField(
            model_name='randomurl',
            name='validity_url',
            field=models.PositiveIntegerField(default=300, validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(30000)], verbose_name='Validity url'),
        ),
    ]
