# Generated by Django 4.0.4 on 2022-05-21 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_alter_tiers_random_expiring_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiers',
            name='random_expiring_url',
            field=models.CharField(choices=[('None', 'None'), ('http://127.0.0.1:8000/bf2fc679155cf67fc3e882608be54a65', 'http://127.0.0.1:8000/bf2fc679155cf67fc3e882608be54a65'), ('http://127.0.0.1:8000/43ddecd4027123df3fceb5507675f1f4ce3e8c03', 'http://127.0.0.1:8000/43ddecd4027123df3fceb5507675f1f4ce3e8c03')], default='None', max_length=255, verbose_name='Random expiring url'),
        ),
    ]