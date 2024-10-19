# Generated by Django 5.1 on 2024-10-08 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='نام برند')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برند ها',
            },
        ),
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
        migrations.AddField(
            model_name='product',
            name='ProductBrand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productbrand', verbose_name='برند محصول'),
        ),
    ]