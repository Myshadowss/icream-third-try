# Generated by Django 4.1.2 on 2022-12-11 09:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_alter_orderaddfield_order_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='order_pack',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='payment.orderpackage'),
        ),
        migrations.AlterField(
            model_name='orderaddfield',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 11, 15, 13, 53, 130402)),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 11, 15, 13, 53, 130402)),
        ),
    ]
