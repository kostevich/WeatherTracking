# Generated by Django 4.2 on 2023-05-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_city_created_at_city_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]