# Generated by Django 4.1.2 on 2022-12-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_offers',
            field=models.IntegerField(default=None),
        ),
    ]