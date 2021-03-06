# Generated by Django 4.0.1 on 2022-03-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_shippingaddress_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': '1. Klienci'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': '3. Zamówienia'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name_plural': '4. Przedmioty z zamówień'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '2. Produkty'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': '5. Adresy dostaw'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_feature',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
