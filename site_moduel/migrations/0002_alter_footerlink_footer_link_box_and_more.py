# Generated by Django 5.1 on 2024-12-10 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_moduel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerlink',
            name='footer_link_box',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='site_moduel.footerlinkbox', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='site_logo',
            field=models.ImageField(upload_to='media', verbose_name='لوگو سایت'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='تغییر اسلایدر'),
        ),
    ]
