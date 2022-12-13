# Generated by Django 4.1.2 on 2022-12-11 09:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_alter_orderaddfield_order_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderaddfield',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 11, 14, 39, 40, 957122)),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 11, 14, 39, 40, 957122)),
        ),
        migrations.AlterField(
            model_name='orderpackage',
            name='is_coupon_apply',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.ordercoupon'),
        ),
    ]