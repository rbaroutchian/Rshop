# Generated by Django 5.1 on 2025-02-09 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0003_alter_orderdetail_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdetails_set', to='order_module.order', verbose_name='سفارش'),
        ),
    ]
