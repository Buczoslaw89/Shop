# Generated by Django 4.0.1 on 2022-02-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_date_order_alter_orderitem_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('W toku', 'W toku'), ('Realizowanie', 'Realizowanie'), ('Zakończone', 'Zakończone')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
