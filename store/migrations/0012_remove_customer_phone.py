# Generated by Django 4.0.1 on 2022-03-01 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_shippingaddress_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
