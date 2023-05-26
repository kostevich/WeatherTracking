# Generated by Django 4.2 on 2023-05-26 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_city_icon_alter_city_id_alter_city_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='city',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
