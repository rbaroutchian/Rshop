# Generated by Django 5.1 on 2024-12-21 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productcategory_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Pcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='Pcategory',
            field=models.ManyToManyField(null=True, related_name='products', to='products.productcategory', verbose_name='دسته بندی'),
        ),
    ]
