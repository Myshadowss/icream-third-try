# Generated by Django 4.1.3 on 2022-11-27 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logins', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productwishlist',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='logins.userinfo'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='product_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='logins.userinfo'),
        ),
        migrations.AddField(
            model_name='productcart',
            name='product_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
        migrations.AddField(
            model_name='productcart',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='logins.userinfo'),
        ),
        migrations.AddField(
            model_name='product',
            name='Cutegory_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
