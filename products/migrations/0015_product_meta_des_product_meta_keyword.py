# Generated by Django 5.1 on 2025-03-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_productbrand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta_des',
            field=models.CharField(blank=True, max_length=300, verbose_name='توضیحات سئو'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keyword',
            field=models.CharField(blank=True, max_length=300, verbose_name='کلمه کلیدی سئو'),
        ),
    ]
