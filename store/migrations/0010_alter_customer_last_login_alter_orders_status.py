# Generated by Django 4.0.6 on 2022-09-10 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_customer_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 10, 18, 7, 39, 181168)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.BooleanField(choices=[('Order Placed', 'ORDER PLACED'), ('Shiped', 'SHIPED'), ('Out for delivery', 'OUT FOR DELIVERY'), ('Delivered', 'DELIVERED'), ('Failed', 'FAILED')], default='Order Placed', max_length=20),
        ),
    ]
