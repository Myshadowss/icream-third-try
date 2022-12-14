# Generated by Django 4.1.2 on 2022-12-10 06:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0001_initial'),
        ('payment', '0008_ordercoupon_alter_orderaddfield_order_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderaddfield',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 10, 12, 11, 33, 571125)),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 10, 12, 11, 33, 571125)),
        ),
        migrations.CreateModel(
            name='OrderPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.IntegerField(default=None)),
                ('is_coupon_apply', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='payment.ordercoupon')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='logins.userinfo')),
            ],
        ),
    ]
