# Generated by Django 4.0.4 on 2022-05-17 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_size_remove_tiers_size_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='tiers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tiers', verbose_name='Tier'),
        ),
    ]
