# Generated by Django 4.0.6 on 2022-09-11 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_delete_shipping_details_orders_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='razorpay_order_id',
            field=models.CharField(default='abcdefghijkl', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 22, 54, 34, 276678)),
        ),
    ]