# Generated by Django 5.1 on 2024-12-22 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_pcategory_product_pcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentcategories', to='products.productcategory'),
        ),
    ]
