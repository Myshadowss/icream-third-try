# Generated by Django 4.1.2 on 2022-12-18 04:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0001_initial'),
        ('payment', '0017_alter_orderaddfield_order_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderaddress',
            name='user_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='logins.userinfo'),
        ),
        migrations.AlterField(
            model_name='orderaddfield',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 18, 10, 15, 14, 132785)),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 18, 10, 15, 14, 132785)),
        ),
    ]
