# Generated by Django 4.1.2 on 2022-12-11 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_orderlist_order_pack_alter_orderaddfield_order_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlist',
            name='order_pack',
        ),
        migrations.AlterField(
            model_name='orderaddfield',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 11, 15, 15, 37, 428518)),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 11, 15, 15, 37, 428518)),
        ),
    ]
